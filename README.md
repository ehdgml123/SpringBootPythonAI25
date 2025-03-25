# SpringBootPythonAI25
스프링부트 와 파이썬을 결합한 AI 풀스택 개발 

스프링부트와파이썬 AI 협업모듈

개발환경구축

파이썬 인터프리터 :  https://www.python.org/downloads/    -> 3.12 버전 설치

IDE 설치 :       https://www.jetbrains.com/ko-kr/pycharm/download/?section=windows          -> 커뮤니티 설치

FastAPI 설치 : pip install fastapi uvicorn uvicorn: ASGI(Asynchronus Server Geteway Interface) 는 파이썬에서 비동기 웹서버 웹 애플리케이션 간 의 인터페이스 표준 ASGI 는 기존 WSGI()Web Server Gateway Interface) 의 비동기
               버전으로 처리를 지원하는 웹 애플리케이션 을 구축하기 위함 https://velog.io/@hwaya2828/WSGI-ASGI


ASGI

비동기 지원 : 비동기 코드 실행을 지원하며 높은 성능과 동시성을 제공, 웹소켓이나 서버 푸시와 같은 비동기 통신이 필요한 애플리케이션에 유용 범용성: HTTP 뿐만 아니라, WebSocket, gPRC 와 같은 다른 프로토로 지원: ASGI 애플리케이션은 다양한
             서버 및 프레임워크 와 호환되먀, 모듈식 으로 구성 FastAPI 와 ASGI


FastAPI 는 ASGI 표준을 따르는 웹 프레임 워크는 FastAPI 애플리케이션은 비동기 처리를 기본으로 하며, uVICORN 과 같은 서버를 사용하여 높은 성능를 제공 FastAPI 서버 실행

main.py 실행  Terminal 에서 D:\pythonWorkSpace > uvicorn main:app -reload --port 8001 (위치확인)
