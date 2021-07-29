import pandas as pd

data_frame = pd.read_csv('../data/friend_list.csv')

# 탭으로 구분된 txt파일 불러오기
# data_frame = pd.read_csv('../data/friend_list_tab.txt', delimiter = '\t')

# head가 없는 csv파일 불러오기
# data_frame = pd.read_csv('../data/friend_list_no_head.csv', header = None, names=['name', 'age', 'job'])
# data_frame.columns = ['name', 'age', 'job']
# print(data_frame)

# print(data_frame)
# print(data_frame.head())
# print(data_frame.tail())
# 데이터프레임은 시리즈의 결합
print('##############################################################################################')

# 시리즈로 데이터프레임을 만들기
s1 = pd.core.series.Series([1, 2, 3])
s2 = pd.core.series.Series( ['one', 'two', 'three'])
data = pd.DataFrame(data = dict(num=s1, word=s2))
# print(data)

friend_dict_list = [ {'name' : 'John', 'age' : 25, 'job' : 'student'},
                     {'name' : 'Nate', 'age' : 30, 'job' : 'teacher'}
]

df = pd.DataFrame(friend_dict_list)

# 딕셔너리는 키값의 순서가 보장되어있지않아 키값의 순서를 지정
df = df[['name', 'age', 'job']]

# 정렬된 딕셔너리
from collections import OrderedDict
friend_ordered_dict = OrderedDict(
    [
        ('name', ['John', 'Nate']),
        ('age', [25, '30']),
        ('job', ['student', 'teacher'])
    ]
)
df = pd.DataFrame.from_dict(friend_ordered_dict)
# print(df)

# 리스트를 사용하여 데이터프레임 만들기
friend_list = [
    ['John', 20, 'student'],
    ['Nate', 30, 'teacher']
]

# 열이름을 부여 (columns를 부여하지않으면 임의로 인덱스가 들어감)
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns= column_name)
# print(df)
print('##############################################################################################')

# 데이터프레임의 구조를 csv파일로 저장하기 (to_csv)
friends = [ {'name':'Jone', 'age':20, 'job':'student'},
            {'name':'Jenny', 'age':30, 'job':None},
            {'name':'Nate', 'age':30, 'job':'teacher'} ]
df = pd.DataFrame(friends)
df = df[[ 'name', 'age', 'job']]
# print(df.head())
df.to_csv('friends.csv')

# 인덱스와 헤더는 디폴드값이 True임
# 행번호를 삭제하고 싶으면 index=False
# 칼럼명(키값)을 삭제하고 싶으면 header=False
# 값이 빈값(None)일때 na_rep= '넣고싶은값'을 넣으면 채워진다
df.to_csv('friends.csv', index= True, header= True, na_rep = '-')
print('##############################################################################################')

# 데이터프레임 행,열(row, column) 선택 및 필터하기
friends = [{'name':'Jone', 'age':20, 'job':'student'},
            {'name':'Jenny', 'age':30, 'job':'developer'},
            {'name':'Nate', 'age':30, 'job':'teacher'}]
df = pd.DataFrame(friends)

# 연속된 특정 row들만 선택하여 필터
# df = df[1:3]

# 특정한 row만 선택하여 필터
# 인덱스로 접근하기위한 loc 메서드
# 0행, 2행만 불러오기
# df = df.loc([0, 2])

# by column condition
# df데이터프레임의 age열의 값이 25보다 큰 행만 선택하여 필터
# df = df[df.age > 25]
# df = df.query('age > 25')
# df = df[ (df.age > 25 & (df.name == 'Nate') ]

# Column을 이용한 필터
# 인덱스로 필터링
friends = [
            ['Jone', 20, 'student'],
            ['Jenny', 30, 'developer'],
            ['Nate', 30, 'teacher']
]
df = pd.DataFrame.from_records(friends)

# 인덱스로 (행, 열)접근하기 위한 iloc 메서드
# 앞부분 행, 뒤부분 컬럼
# print(df.iloc[:, 0:2])
# print(df.iloc[0:2, 0:2])

# 컬럼명으로 필터링
df = pd.read_csv('../data/friend_list_no_head.csv', header=None, names=['name', 'age', 'job'])
# name, age 칼럼만 가져오기
df_filtered = df[['name', 'age']]
# print(df_filtered)
# df = df.filter(items=['age', 'job'])
# print(df)

# 칼럼명에 a가 들어노는 칼럼만 가져오고싶으면
# df = df.filter(like='a', axis=1) # axis=1은 열
# print(df)

# 정규식 사용
# 칼럼명이 b로 끝나는 칼럼만 가져옴
print(df.filter(regex='b$', axis=1))
