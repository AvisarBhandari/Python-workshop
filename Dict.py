student = {'name':'Kashi','age':'69','grade':'A'}

print('Keys:',student.keys())
print('Values:',student.values())
print('Items:',student.items())
print('Grade:',student.get('grade'))
student.pop('age')
print('After poping age:',student)
