open("/home/caratred/ezygst_bench/sites/rgst.com/private/files/d140/HRCHANDIGARH/022024.txt","a+").close()
with open("/home/caratred/Downloads/022024 (1).txt","r") as text_file:
    text_file = text_file.readlines()
    for i in text_file:
        with open("/home/caratred/ezygst_bench/sites/rgst.com/private/files/d140/HRCHANDIGARH/022024.txt","a+") as app:
            app.write(i)