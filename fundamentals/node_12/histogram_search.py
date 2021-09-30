'''
1. 프로그램 실행
2. 입력된 경로 이미지 파일 불러오기
3. 검색 대상 이미지들 중 불러온 이미지와 가장 비슷한 이미지 5개 표시
4. 프로그램 종료
->
1. 프로그램 실행
2. 입력된 경로 이미지 파일 불러오기
3. 검색 대상 이미지들 중 불러온 이미지와 가장 비슷한 이미지 5개 고르기
- 검색 대상 이미지 불러오기
- 입력 이미지와 비교하여 유사도 기준으로 순서 매김
    - 입력 이미지와 검색 대상 이미지들 사이 유사도 계산
        - 입력 이미지와 검색 대상 이미지 모두 히스토그램 만들기
        - OpenCV의 compareHits() 함수로 히스토그램간 유사도 계산
    - 계산된 유사도를 기준으로 정렬하여 순서 매김
- 유사도 순서 상 상위 5개 이미지 고르기
4. 고른 이미지 표시
5. 프로그램 종료
'''
print("안녕")