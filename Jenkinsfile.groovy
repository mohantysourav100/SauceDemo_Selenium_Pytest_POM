pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Parallel Cross-Browser Tests') {
            parallel {
                stage('Chrome Tests') {
                    steps {
                        bat '''
                        call venv\\Scripts\\activate
                        pytest -n 2 --browser_name=chrome -v -s --html=reports/chrome_report.html --self-contained-html --alluredir=allure-results --capture=tee-sys
                        '''
                    }
                }
                stage('Firefox Tests') {
                    steps {
                        bat '''
                        call venv\\Scripts\\activate
                        pytest -n 2 --browser_name=firefox -v -s --html=reports/firefox_report.html --self-contained-html --alluredir=allure-results --capture=tee-sys
                        '''
                    }
                }
                stage('Edge Tests') {
                    steps {
                        bat '''
                        call venv\\Scripts\\activate
                        pytest -n 2 --browser_name=edge -v -s --html=reports/edge_report.html --self-contained-html --alluredir=allure-results --capture=tee-sys
                        '''
                    }
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
         }
       stage('Publish HTML Reports') {
        steps {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'chrome_report.html, firefox_report.html',
                reportName: 'Cross Browser Test Report'
            ])
        }
      }
    }
}