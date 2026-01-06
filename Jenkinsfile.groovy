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
                        pytest -n 2 --browser_name=chrome -v -s --html=reports/report.html --self-contained-html --alluredir=allure-results --capture=tee-sys
                        '''
                    }
                }
                stage('Firefox Tests') {
                    steps {
                        bat '''
                        call venv\\Scripts\\activate
                        pytest -n 2 --browser_name=firefox -v -s --html=reports/report.html --self-contained-html --alluredir=allure-results --capture=tee-sys
                        '''
                    }
                }
                stage('Edge Tests') {
                    steps {
                        bat '''
                        call venv\\Scripts\\activate
                        pytest -n 2 --browser_name=edge -v -s --html=reports/report.html --self-contained-html --alluredir=allure-results --capture=tee-sys
                        '''
                    }
                }
            }
        }
    }
}