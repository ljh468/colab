import pandas as pd

print('##############################################################################################')

# 중복 데이터 삭제하기
student_list = [{'name': 'John', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Nate', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Abraham', 'major': "Physics", 'sex': "male"},
                {'name': 'Brian', 'major': "Psychology", 'sex': "male"},
                {'name': 'Janny', 'major': "Economics", 'sex': "female"},
                {'name': 'Yuna', 'major': "Economics", 'sex': "female"},
                {'name': 'Jeniffer', 'major': "Computer Science", 'sex': "female"},
                {'name': 'Edward', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Zara', 'major': "Psychology", 'sex': "female"},
                {'name': 'Wendy', 'major': "Economics", 'sex': "female"},
                {'name': 'Sera', 'major': "Psychology", 'sex': "female"},
                {'name': 'John', 'major': "Computer Science", 'sex': "male"},
         ]
df = pd.DataFrame(student_list, columns = ['name', 'major', 'sex'])

# 중복데이터 index 조회
df.duplicated()
# 데이터프레임에서 중복데이터 제거하기
# print(df.drop_duplicates())

# name이 같을때 나중에 나오는 데이터를 제거하기
student_list = [{'name': 'John', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Nate', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Abraham', 'major': "Physics", 'sex': "male"},
                {'name': 'Brian', 'major': "Psychology", 'sex': "male"},
                {'name': 'Janny', 'major': "Economics", 'sex': "female"},
                {'name': 'Yuna', 'major': "Economics", 'sex': "female"},
                {'name': 'Jeniffer', 'major': "Computer Science", 'sex': "female"},
                {'name': 'Edward', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Zara', 'major': "Psychology", 'sex': "female"},
                {'name': 'Wendy', 'major': "Economics", 'sex': "female"},
                {'name': 'Nate', 'major': None, 'sex': "male"},
                {'name': 'John', 'major': "Computer Science", 'sex': None},
         ]
df = pd.DataFrame(student_list, columns = ['name', 'major', 'sex'])

# name이 중복된데이터 index 조회
# print(df.duplicated('name'))

# 처음나오는 name은 유지 (기본값은 first)
# print(df.drop_duplicates('name'), keep='first')

print('##############################################################################################')
# NaN (None)찾아서 다른 값으로 변경하기
school_id_list = [{'name': 'John', 'job': "teacher", 'age': 40},
                {'name': 'Nate', 'job': "teacher", 'age': 35},
                {'name': 'Yuna', 'job': "teacher", 'age': 37},
                {'name': 'Abraham', 'job': "student", 'age': 10},
                {'name': 'Brian', 'job': "student", 'age': 12},
                {'name': 'Janny', 'job': "student", 'age': 11},
                {'name': 'Nate', 'job': "teacher", 'age': None},
                {'name': 'John', 'job': "student", 'age': None}
         ]
df = pd.DataFrame(school_id_list, columns = ['name', 'job', 'age'])
# None값 조회하기
# print(df.info())
# None값 테이블로 조회하기
# print(df.isna())

# None값을 0으로 변경하기
# df.age = df.age.fillna(0)

# None값을 median 값으로 변경하기
# job으로 그룹짓고 age가 None값을 job별 중간값으로 변경
df.age = df.age.fillna(df.groupby('job')['age'].transform('median'))
# print(df)

print('##############################################################################################')
# apply함수, 다양한 예제로 활용
date_list = [{'yyyy-mm-dd': '2000-06-27'},
         {'yyyy-mm-dd': '2002-09-24'},
         {'yyyy-mm-dd': '2005-12-20'}]
df = pd.DataFrame(date_list, columns = ['yyyy-mm-dd'])
print(df)