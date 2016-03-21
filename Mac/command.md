#Mac 日常应用


## 卸载一个pkg 包


```
$ pkgutil --pkgs  #list all installed packages
$ pkgutil --files the-package-name.pkg     #list installed files
$ pkgutil --pkg-info the-package-name.pkg  #check the location
$ cd /    #assuming the package is rooted at / ...
$ pkgutil --only-files --files the-package-name.pkg |tr '\n' '\0' | xargs -n 1 -0 sudo rm -i
$ pkgutil --only-dirs --files the-package-name.pkg | tr '\n' '\0' | xargs -n 1 -0 sudo rm -ir
$ sudo pkgutil --forget the-package-name.pkg
```
