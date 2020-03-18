from colorama import init
from colorama import Fore, Back, Style
import random
init()
position_list=[] # stores postion of queen in list format
				 # list containing n lists, 
				 #for example postion_list is [[1, 3], [2, 2], [3, 1], [4, 1]] for 4 queens where each list is in [column,row] format
				 # constarint::-> every column must contain only one queen, but one row may contain more than one queen
				 # so queen of 1st column is in 3rd row
				 # so queen of 2nd column is in 2nd row
				 # so queen of 3rd column is in 1st row
				 # so queen of 4th column is in 1st row
intial_state=[] # store intial postion of list i.e given prblm statement
attacking_pairs=[] # stores attcking pairs for a particular postion_list
				   # for example [[2,3],[4,5],[6,7]] total attcking pair is 3
				   # so queen of 2nd column is attacking queen of 3rd column and viceversa
				   # so queen of 4th column is attacking queen of 5th column and viceversa
				   # so queen of 6th column is attacking queen of 7th column and viceversa

def solve_N_queen():
	attack_count=len(attacking_pairs)
	for i in range(n):
		#print('Queen ',i+1,' is now moving')
		col=position_list[i][0]
		row=position_list[i][1]
		temp=row
		for j in range(n):
			if (j+1)==row:
				continue
			position_list[i][1]=j+1
			#print_board()
			attacking_pairs_print()
			if len(attacking_pairs)<=attack_count:  # two different implementation (<,<=)
				attack_count=len(attacking_pairs)
				temp=j+1
		position_list[i][1]=temp
		#print(Fore.CYAN)
		#print('best position for queen ',i+1)
		#print_board()
		attacking_pairs_print()
		#print(Style.RESET_ALL)

				
def attacking_pairs_print():
	global attacking_pairs
	attacking_pairs=[]
	count=0
	for i in range(n):
		col=position_list[i][0]
		row=position_list[i][1]
		j=i+1
		while(j<n):	
			col1=position_list[j][0]
			row1=position_list[j][1]
			if row1==row:
				count+=1
				attacking_pairs.append([col,col1])
			elif abs(row-row1)==abs(col-col1):
				count+=1
				attacking_pairs.append([col,col1])
			j+=1
	#print('total no of attacking pairs : ',count)
	#print('attacking pairs are : ',attacking_pairs)





def print_board():
	for i in range(n):
		print( '.___',end='')
		if i==n-1:
			print('.')

	for i in range(n):
		temp=[]
		for k in range(n):
			if position_list[k][1]==(i+1):
				temp.append(k+1)
		#print(temp)
		for j in range(n+1):
			if j==n:
				print('|')
			elif (j+1) not in temp:
				print('|___',end='')
			else:
				print('|_*_',end='')
				temp.pop(0)

def matrix_copy_function(list):
	for i in position_list:
		list.append(i.copy())


def complete():
	global temp_list
	for i in range(100):
		solve_N_queen()
		#print(Fore.GREEN)
		#print('AFTER ',i+1,' EPOCH')
		#print_board()
		attacking_pairs_print()
		#print(Style.RESET_ALL)

		if len(attacking_pairs)==0:
			return 1

		elif temp_list==position_list:
			print(temp_list,'\n',position_list)
			return 'stuck'

		temp_list=[]
		matrix_copy_function(temp_list)
	if i==99:
		print('cycles over')
		return 'cycleover'



# execution starts from here

print('constarint::-> every column must contain only one queen, but one row may contain more than one queen')
n=int(input('enter the number of queens :'))
result_of_20_runs=[]
temp_list=[]
for i in range(20):
	for j in range(n):
		position_list.append([(j+1),random.randrange(1,(n+1),1)])
	print('INITIAL STATE')
	print_board()
	attacking_pairs_print()
	temp_list=[]
	matrix_copy_function(temp_list)
	#matrix_copy_function(intial_state)
	res=complete()
	result_of_20_runs.append(res)
	position_list=[]

print(result_of_20_runs)
print('success ratio : ',result_of_20_runs.count(1)/20)
