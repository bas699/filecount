#https://qastack.jp/programming/2632205/how-to-count-the-number-of-files-in-a-directory-using-python

import os,tkinter,tkinter.filedialog,pathlib,sys,io
def get_dir_size(path='.'):
	total=0
	try:
		with os.scandir(path) as it:
			for entry in it:
				if entry.is_file():
					total += entry.stat().st_size
				elif entry.is_dir():
					total += get_dir_size(entry.path)
	except OSError as err:
		print(err)
		pass
	return total
	
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
root = tkinter.Tk()
root.withdraw()
fTyp =[("","*")]
iDir=os.path.abspath(os.path.dirname(__file__))
print("対象フォルダを選んでください")

dir=tkinter.filedialog.askdirectory(initialdir = iDir)
dirs = []
for filename in os.listdir(dir):
	if os.path.isdir(os.path.join(dir, filename)):
		dirs.append(filename)
print(dir)
with open("export.txt","wt") as fp:
	for c_dir in dirs:
		print(c_dir)
		file_count = sum(len(files) for _, _, files in os.walk(os.path.join(dir,c_dir)))
		kekka = "フォルダ："+c_dir+"　ファイル数："+str(file_count)+"　サイズ："+str(get_dir_size(os.path.join(dir,c_dir)))
		print(kekka)
		print(kekka,file = fp)
