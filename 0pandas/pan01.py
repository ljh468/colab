import pandas as pd

data_frame = pd.read_csv('../data/friend_list.csv')
# 데이터프레임 행, 열 삭제하기
friends = [{'age': 15, 'job': 'student'},
           {'age': 25, 'job': 'developer'},
           {'age': 30, 'job': 'teacher'}]

df = pd.DataFrame(friends,
                  index=['John', 'Jenney', 'Nate'],
                columns=['age', 'job'])
# print(df)

# 특정 행의 데이터 삭제하기 drop(인덱스 이름을 넣어줌)
# print(df.drop(['John', 'Nate']))

# drop한 데이터를 바로 적용하려면
# df.drop(['John', 'Nate'], inplace= True)
# print(df)

friends = [{'name': 'John', 'age': 15, 'job': 'student'},
           {'name': 'Jenney', 'age': 25, 'job': 'developer'},
           {'name': 'Nate', 'age': 30, 'job': 'teacher'}]
df = pd.DataFrame(friends, columns=['name','age', 'job'])
# print(df)
# row의 인덱스로 삭제하려면
# print(df.drop(df.index[[0, 2]]))

# 조건으로 삭제하기
# column의 값에 따른 삭제
df = pd.DataFrame(friends, columns=['name', 'age', 'job'])
df_20 = df[df.age > 20]

# age 컬럼을 삭제하려면 (열이라고 지정해줘야함)
# print(df.drop('age', axis=1))

print('##############################################################################################')
# 행, 열 생성 및 수정하기 (row, column, update)
friend_dict_list = [ {'name': 'Jone', 'age': 15, 'job': 'student'},
                     {'name': 'Jenny', 'age': 30, 'job': 'developer'},
                     {'name': 'Nate', 'age': 30, 'job': 'teacher'}]
df = pd.DataFrame(friend_dict_list, columns=['name', 'age', 'job'])

# salary 열 추가하기
df['salary'] = 0
# numpy를 이용하여 salary열의 값 수정
# np.where(condition, T, F) 값 변경
# job이 student가 아니면 yes 맞으면 no ( np.where() )
import numpy as np
df['salary'] = np.where(df['job'] != 'student', 'yes', 'no')

# 시험성적 데이터프레임 만들기
friend_dict_list = [ {'name': 'Jone', 'midterm': 95, 'final': 85},
                     {'name': 'Jenny', 'midterm': 85, 'final': 80},
                     {'name': 'Nate', 'midterm': 30, 'final': 10}]
df = pd.DataFrame(friend_dict_list, columns=['name', 'midterm', 'final'])

# 종합점수 컬럼 추가하기
df['total'] = df['midterm'] + df['final']

# 평균점수 컬럼 추가하기
df['average'] = df['total'] / 2

# 학점 컬럼 추가하기
grades = []
for row in df['average']:
    if row >= 90:
        grades.append('A')
    elif row >= 80:
        grades.append('B')
    else :
        grades.append('F')
# 리스트에 담긴 값 넣기
df['grade'] = grades

# grade컬럼을 합격, 불합격 컬럼으로 변경하기
def pass_or_fail(row):
    if row != 'F':
        return 'Pass'
    else:
        return 'Fail'

# apply()는 grade 컬럼의 각 값을 인자로 넣어줌
# 정해놓은 함수 return값을 일괄적으로 적용
# df.grade = df.grade.apply(pass_or_fail)

# 람다함수를 이용하여 apply ( lambda x가 F가 아니면 pass, F면 fail )
df['grade'] = df.grade.apply(lambda x:'Pass' if x!='F' else 'Fail')
# print(df)

date_list = [
    {'yyyy-mm-dd': '2000_06_27'},
    {'yyyy-mm-dd': '2007_10_27'}
]
df = pd.DataFrame(date_list, columns= ['yyyy-mm-dd'])

# 연도만 뽑아내기 위한 메서드
def extract_year(row):
    return row.split('_')[0]

# 년도만 나오는 컬럼 추가하기
df['year'] = df['yyyy-mm-dd'].apply(extract_year)

# 행 추가하기
friend_dict_list = [{'name': 'Jone', 'midterm': 95, 'final': 85},
                    {'name': 'Jenny', 'midterm': 85, 'final': 80},
                    {'name': 'Nate', 'midterm': 30, 'final': 10}]
df = pd.DataFrame(friend_dict_list, columns=['name', 'midterm', 'final'])
df2 = pd.DataFrame([ ['Ben', 50, 50] ], columns=['name', 'midterm', 'final'])

# 오리지널과 성적점사 합치기
# df2의 인덱스는 제거하고 추가
# print(df.append(df2, ignore_index = True))

print('##############################################################################################')
# 데이터 그룹 만들기
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
                {'name': 'Sera', 'major': "Psychology", 'sex': "female"}
         ]
df = pd.DataFrame(student_list, columns=['name', 'major', 'sex'])

# 학과별 인원수로 group by
# group_by 사용하기
group_by_major = df.groupby('major')
# print(group_by_major)
# group_by_major의 그룹확인
# print(group_by_major.groups)

# for문으로 알아보기 쉽게 시각화함
for name, group in group_by_major:
    print(name + ':' + str(len(group)))
    print(group)
    print()

# 학과별로 데이터프레임 만들기
df_major_cnt = pd.DataFrame({'count': group_by_major.size()}).reset_index()
# print(df_major_cnt)

print('##############################################################################################')
# 성별로 group by
group_by_sex = df.groupby('sex')
# for name, group in group_by_sex:
#     print(name + ':' + str(len(group)))
#     print(group)
#     print()

# 성별로 데이터프레임 만들기
df_sex_cnt = pd.DataFrame( {'count' : group_by_sex.size()}).reset_index()
# print(df_sex_cnt)