이기프트샵 BO FO 셋팅설정

안녕하십니까. 신세계 아이앤씨 강성태입니다.



BO + FO 개발환경 구축방법 및 JDK 설치파일 경로(VDI 공유폴더) 를 전달드리오니 확인 부탁드립니다.



** BO **

\1. 이클립스 window → preferenced 內 settings.xml 적용 후 → maven install → maven update (참고사이트 : https://lovelytney.tistory.com/14)

\2. swaf-mon-mvc 內 enc~Path : 1.txt ~ 2.txt 프로젝트 內 파일 검색하여 로컬 폴더 경로로 수정

\3. GiftShopBiApplication.java 실행

\4. localhost:8484 호출 시 BO 화면 확인

  관리자 접속 ID : admin / pw : 1

  유저 접속 ID : gsadmin / pw : gsadmin12!@



** FO **

\1. 프로젝트 git pulling 후 settings.xml 로 메이븐 설정 
  ※ log cannot be resolved 에러 발생 시 lombock 재등록 후 프로젝트 refresh
  (재등록 법 : Maven-Dependencies - lombock~.jar 마우스 우클릭 - run as java application - specify location 버튼 선택 - 이클립스.ini 찾아서 선택 - install 버튼
 
\2. swaf-mon-mvc 內 spring.profils.active 설정 환경에 맞게 (필자는 local로 수행)
  enc~Path : 1.txt ~ 2.txt 프로젝트 內 파일 검색하여 로컬 폴더 경로로 수정
\3. GiftshopFrontApplication.java 실행
\4. localhost:9494 호출 시 testest 텍스트 출력 여부 확인





** JDK 설치파일 경로 **



※  [\\sgpvdifs01\Gift](file://sgpvdifs01/Gift) 배송서비스 도입 프로젝트\99.개인폴더\기타\공유



감사합니다.