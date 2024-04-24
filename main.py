import time
import lzma # cel mai bun si cel mai incet
import gzip # mediocru si incet
import bz2 # mediul si super rapid
import multiprocessing as mp

def worker(text0,text1):
    with open(text0, 'rb') as f_in, gzip.open(text1, 'wb') as f_out:
        f_out.write(f_in.read())

# BZ2
if __name__ == '__main__':
    start = time.time()

    t0 = mp.Process(target=worker, args=('text0.txt','ifile0.xz'))
    t1 = mp.Process(target=worker, args=('text1.txt','ifile1.xz'))
    t2 = mp.Process(target=worker, args=('text2.txt','ifile2.xz'))
    t3 = mp.Process(target=worker, args=('text3.txt','ifile3.xz'))
    t4 = mp.Process(target=worker, args=('text4.txt','ifile4.xz'))
    t5 = mp.Process(target=worker, args=('text5.txt','ifile5.xz'))
    t6 = mp.Process(target=worker, args=('text6.txt','ifile6.xz'))

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    end = time.time()
    print(end-start)

    start = time.time()
    with open('text0.txt', 'rb') as f_in, gzip.open('file0.xz','wb') as f_out:
        f_out.write(f_in.read())
    with open('text1.txt', 'rb') as f_in, gzip.open('file1.xz','wb') as f_out:
        f_out.write(f_in.read())
    with open('text2.txt', 'rb') as f_in, gzip.open('file2.xz','wb') as f_out:
        f_out.write(f_in.read())
    with open('text3.txt', 'rb') as f_in, gzip.open('file3.xz','wb') as f_out:
        f_out.write(f_in.read())
    with open('text4.txt', 'rb') as f_in, gzip.open('file4.xz','wb') as f_out:
        f_out.write(f_in.read())
    with open('text5.txt', 'rb') as f_in, gzip.open('file5.xz','wb') as f_out:
        f_out.write(f_in.read())
    with open('text6.txt', 'rb') as f_in, gzip.open('file6.xz','wb') as f_out:
        f_out.write(f_in.read())

    end = time.time()
    print()
    print(end-start)