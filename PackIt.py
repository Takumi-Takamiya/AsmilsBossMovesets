import zipfile,os,queue

##zip_f=zipfile.ZipFile("./compressed.zip",'w')

for text in os.listdir():
    path=os.path.join(".",text)
    if os.path.isdir(path):
        print(path)
        print(path+'.zip')
        zip_f=zipfile.ZipFile(path+'.mcpack','w')
        q = queue.Queue()
        q.put(path)
        while not q.empty():
            p=q.get()
            for sub in os.listdir(p):
                np=os.path.join(p,sub)
                zip_f.write(np)
                if os.path.isdir(np):
                    q.put(np)

zip_f.close()