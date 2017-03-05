multiStr = "select * from multi_row \
where row_id < 5"
print(multiStr)
 
# select * from multi_row where row_id < 5

multiStr = """select * from multi_row 
where row_id < 5"""
print(multiStr)
 
#select * from multi_row 
#where row_id < 5



#solution is to split the string into multi lines and enclose the entire string in parenthesis.

multiStr= ("select * from multi_row "
"where row_id < 5 "
"order by age") 
print(multiStr)
 
#select * from multi_row where row_id < 5 order by age
