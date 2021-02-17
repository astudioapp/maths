import os
replacement = "to 2 decimal places"
for dname, dirs, files in os.walk("/mnt/e/local git/astudio/maths/equations"):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
        s = s.replace("to 2 decimal places", replacement)
        with open(fpath, "w") as f:
            f.write(s)