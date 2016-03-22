# Go 学习笔记

## Go程序设计的一些规则
   Go之所以那么简单,因为它有一些默认的行为: - 大写字母开头的变量是可以导出的,也就是其它包可以读取的,是公用变量.小写字母开头的就是不可导出的,是私有变量. - 大写字母开头的函数也是一样,相当于class中的带public关键词的公有
   函数;小写字母开头的函数就是有private关键字的私有函数.

## 变量

#### 变量定义
   在Go语言中,无论变量赋值、import 导入package.都需要被使用,如果只是导入而不使用,那么在编译的时候会报错.

```
var  变量名 类型 ＝ 变量值
var  变量名 ＝ 变量值
变量名 := 变量值   ＃:= 取代了var 和type.这种赋值方式只能在函数体内定义,如果在函数体外定义,编译的时候会报错.
_, 变量名 := var1, var2   #_(下划线)是个特殊的变量名,任何赋给它的值都会丢弃.
``` 

## 常量
   常量是在程序编译之前已经确定下来的值.而程序在运行过程中无法更改它的值.在Go中,常量可以定义为整值、字符串、布尔值等.

```
const name = "sina"
const name = 123
const name = '1.2431'
const name = false
```



##内置数据类型

### Boolean
   在Go中,布尔值的类型为bool,值是true或false,默认值为false.

```
var name bool   #一般声明,默认false
name = true     #赋值操作
name := false   #简短声明
```

### 数值类型
   整数类型有无符号和带符号两种.Go同时支持int和uint,这两种类型的长度相同,但具体长度取决于不同编译器的实现.当前的Gcc和Gccgo编译器在32位和64位平台上都适用32位来表示int和uint,但未来在64位平台上可能增加到64位.Go
   里面也有直接定义好位数的类型:rune、int8、int16、int32、int64和byte、uint8、uint16、uint32、uint64.
   其中rune是int32的别称,byte是uint8的别称.

   这些类型的变量之间不允许相互赋值或操作,不然会在编译时引起编译器报错.
   尽管int的长度是32bit,但int与int32并不能互用.
   浮点数的类型有float32和float64两种(没有float类型),默认是float64.
   Go还支持复数,它的默认类型是complex128(64位实数+64位虚数).

```
var number int = 12       			// number := 12
var float float64 = 3.1415926  		// float :=3.1415926
var cpx complex128 = 1 + 5i			// cpx := 1 + 5i
```

### 字符串
    Go的字符串都是采用utf-8字符集编码.字符串时用一对双引号("")或反引号(``)扩起来定义,它的类型是string.

```
var str string = "Hello World!"  // str := "Hello World!"
var str string                   // 声明类型但未赋值.
string ＝ "Hello World!"         // 赋值

# 字符串替换
# go字符串类型是不可变的,如果要想做字符串替换.需要借助slice进行替换.
s := "Hello"
c := []byte(s)
c[0] = 'C'
s1 := string(c)                   // 这样实现了字符串的替换

＃或者使用这种方式进行字符串替换
s := "Hello World!"
s = "C" + s[1:]
fmt.Print(s)

#字符串连接
s := "Hello"
m := "World!"
a := s + m
fmt.Print(a)

#如何声明一个多行字符串,在python中用''' ''' 来实现多行的实现.Go中可以使用反括号实现.
var name string = ` Hello
            World!
            `
```    

### 错误类型
    我感觉Go中对异常处理还是比较弱的,没有向Python 提供内置的try...except 实现异常处理.Go 内置有一个error类型.Go的标准库里还有一个errors来处理异常.

```
import (
    "errors"
)

err := errors.New("emit macho dwarf: elf header corrupted.")
if err != nil {
	fmt.Print(err)
}
```

### array
    array 数组,在python中它被叫列表.

    定义语法:
    var 变量名称 [n]类型
     
    在[n]type中, n 表示数组的长度,type表示存储元素的类型.对数组的操作和其它语言类似.都是通过[]进行读取或赋值.

    在Golang中,数组也是不能改变的长度.因此[3]int 与 [4]int 是不同的类型.数组之间的赋值是值的赋值,即当把一个数组作为参数传入函数的时候,传入的其实是该数组的副本,而不是它
    的指针。如果要使用指针,就需要用到后面的slice类型.

 ```
 var arr [10]string      // 声明一个数组,数组的元素是字符串类型.
 arr[0] = "David"		 // 给数组元素赋值
 arr[1] = "12"           // 给数组元素赋值

 #或者这样定义一个数组
 arr := [10]string{"David", "12"}
 ```
 Go还支持多维数组,即多维数组.
 ```
 arr := [2][4]int{[4]int{1,2,3,4}, [4]int{5,6,7,8}}
 # 如果内部的元素和外部的一样, 直接可以忽略内部的类型
 arr := [2][4]int{{1,2,3,4}, {5,6,7,8}}
 ```

 ### slice
    在很多场景中,数组并不能满足我们的需求.在初始定义数组时,我们并不知道需要多大的数组,因此我们就需要"动态数组".在Go里面这种数据结构叫slice.

    slice并不是真正意义上的动态数组,而是一个引用类型.slice总是指向一个底层array,slice的声明也可以像array一样,只是不需要长度.

```
arr := []byte{'a', 'b', 'c', 'd'} 
```
