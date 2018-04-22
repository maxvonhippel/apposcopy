import hashlib
import sys


#Get md5 of apk file.
def getmd5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

def main(argv):
    fname = argv[0]
    md5 = getmd5(fname)
    print md5

if __name__ == "__main__":
    main(sys.argv[1:])
