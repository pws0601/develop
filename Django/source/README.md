1. django-admin startproject <프로젝트명> .
  - ex django-admin startproject do_it_django_prj .

 2. python manage.py runserver
  - ex python manage.py runserver 0.0.0.0:8000 : 외부 접속 가능하게 django server 구동

  3. python manage.py migrate 
  - 데이터베이스 생성
  
  4. python manage.py createsuperuser
  - 관리자 계정 생성하기

  5. python manage.py startapp <app 이름>
  - app 만들기
  - ex python manage.py startapp blog
  - ex python manage.py startapp single_pages

  6. python manage.py makemigrations
  - 데이터베이스에 변경 모델 반영
  - python manage.py migrate : 변경모델 반영 후 적용

  7. settings.py
  - App 등록
    INSTALLED_APPS = [
    ....
    'app 등록',
    ]
  - 그리니치 표준시에서 기준 시간을 서울로 변경
    TIME_ZONE = 'UTC'
    TIME_TZ = TRUE
    => TIME_ZONE = 'Asia/Seoul'
    => TIME_TZ = False


