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

# slice(切片)
    在很多应用场景,数组并不能满足我们的需求。在初始定义数组时,我们并不知道需要多大的数组,因此我们就需要"动态数组".在Go里面这种数据结构叫slice.

    slice并不是真正意义上的动态数组,而是一个饮用类型.slice总是指向一个底层的array,slice的声明也可以像array一样,只是不需要长度.
    
    append()函数会改变slice所引用的数组的内容，从而影响到引用同一数组的其它slice.但当slice中没有剩余空间时,此时将动态分配新的数组空间.返回的slice数组指针将指向这个空间,而原数组的内容将保持不变;其它引用此数组的slice则不受影响.
    
```
var numbers []int                    //声明一个int类型的slice.
numbers ＝ append(numbers, 2)        //新增加一个元素
numbers ＝ append(numbers, 2,3,4)   //新增多个元素

numbers := []int{1,2,3}              //另外一种常见slice方式

＃切片截取
arr := [10]int{1,2,3,4,5,6,7,8,9,10}    //创建一个数组
var numbers []int                       //定义一个slice
numbers = arr[1:4]                      //初始化一个slice
numbers = arr[:]
numbers = arr[0:]
```
    
## slice 和 array区别
    slice和数组在声明时的区别：声明数组时,方括号内写明了数组的长度和使用...自动计算长度,而声明slice时,方括号内没有任何符号.
    

```
var a int[]
var b int[]
arr := [10]int{1,2,3,4,5,6,7,8,9,10}
a = arr[:]
b = arr[:]
a[0] = 10
printSlice(a)
printSlie(b)

func printSlice(x []int){
    println(x)
}
```
   slice是引用类型,所以当引用改变其中元素的值时,其它的所有引用都会改变该值.
   
# map
   map 也就是python中字典的概念,它的格式为map [keyType]valueType
   
```
var numbers map[string]string
numbers = make(map[string]string)
numbers["name"] = "David"
numbers["sex"] = "boy"
for key, value := range numbers {
    Printf("%v => %v\n", key, value)
}

或者:
numbers := make(map[string]string)
numbers["name"] = "David"
numbers["sex"] = "boy"
for key, value := range numbers {
    Printf("%v => %v\n", key, value)
}

numbers := map[string]string {"name" : "david", "sex": "boy"}   //初始化一个字典

value, status = numbers['name']
map 返回两个值,第二个返回值,如果不存在key,那么status为false.如果存在status为true.

delete(numbers, "name")     //删除numbers map里的name元素.

``` 

# 流程控制和函数
   流程控制包含分三大类: 条件判断、循环控制和无条件跳转
   

## if
     Go里面if条件判断语句中不需要括号:

```
if x > 10 {
    println("xxx")
} else {
    println("kkk")
}
```   

Go的if还有一个强大的地方就是条件判断语句里面允许声明一个变量，这个变量的作用域只能在该条件逻辑块内,其他地方就不起作用了.

```
if x := fun(); x > 10 {
    println("xxx") 
} else {
    println("ooo")
}
```

多条件判断:

if integer == 3 {
    println("xxx")
} else if integer < 3 && integer > 5 {
    println("OOOOO")
} else {
    println("kkkk")
}


## goto
   Go有goto语句.用goto跳转到必须在当前函数内定义的标签.
   
```
func main() {
    var num int = 0

Here:
    for num < 10 {
        if num == 5 {
            num++
            goto Here
        }
        println(num)
        num++
    }
}
```

在这个例子中,类似于continue功能.这里一定要谨慎使用,防止变成一个死循环。在开发中还是不建议使用goto

## for
   Go里面最强大的一个控制逻辑就是for,它即可以用来循环读取数据,又可以当作while来控制逻辑,还能迭代操作.语法如下:
   
```
for expression1; expression2; expression3 {
     //...
}
```

expression1、expression2和expression3都是表达式,其中expression1 和expression3是变量声明或者函数调用返回值之类的,expression2是用来条件判断,expression1在循环开始之前调用,expression3在每轮循环结束时调用.

```
package main

func main() {
    sum := 0
    for index := 0; index <10; index++ {
        sum++
    }
    println(sum)
}
```
有些时候如果我们忽略expression1 和expression3,其实这就是一个while的功能:

```
sum := 1
for sum < 1000 {
    sum++
}
```

### continue和break
    在循环里面有两个关键字break 和 continue.break操作时跳出当前循环,continue时跳过本次循环.当嵌套过深的时候,break可以配合标签使用,即跳转至标签所指定的位置.
    

Go支持"多值返回",而对于"声明而未被调用"的变量,编译器会报错,在这种情况下,可以使用_来丢弃,不需要返回值.

```
numbers := []int{1,2,3,4,5,6}
for _, value := range numbers {
    println(value)
}
```

## switch
    有时候需要很多if...else if判断,而且判断的结果比较明确.可以使用switch来实现.语法:

```
switch sExpr {
    case expr1:
        do something
    case expr2:
        do something
    case expr3:
        do something
    case expr4:
        do something
    default:
        do something
}
```
   sExpr和expr1、expr2...exprn的类型必须一致.Go的swith非常灵活,表达式不必是常量或者整数,执行的过程从上至下,直到找到匹配项:
   
```
i := 10
switch i {
    case 1,2,3,4:
        println("less 5")
    case 5,6,7,8,9:
        println("less 10")
    case 10:
        println("eq 10")
    default:
        println("the interage Error.")
}
```
    我们很多值聚合在了一个case里面,Go里面switch 默认相当于每个case最后带有break,匹配成果后会不会自动向下执行其它case,而是跳出switch,但是可以使用fallthrough强制执行后面的case代码.
    

#函数
   函数是Go里面的核心设计,它通过关键字func来声明,它的格式如下：
   
```
func funcName (input1 type1, input2 type2) (output1 type1, outpu2 type2) {
    return value1, value2
}
```
> 关键字func用来声明一个函数funcName

> 函数可以有一个或者多个参数,每个参数后面带有类型,通过, 分隔.

> 函数可以返回多个值

> 上面返回值声明了两个变量output1 和 output2,如果你不想声明也可以,直接就两个类型

> 如果只有一个返回值且不声明返回值变量,那么你可以省略 包括返回值的括号

> 如果没有返回值，那么久直接省略最后的返回信息

> 如果有返回值，那么必须在函数的外层添加return语句


```
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    x := max(4,5)
    println(x)
}
```
这个函数只有一个返回值.max函数有两个参数,它们的类型都是int,第一个变量的类型可以省略,默认为离它最近的类型,同理多于2个同类型的变量或者返回值，我们也可以这样写.

### 多个返回值
    Go 语言比C更先进的特性,其中一点就是函数能够返回多个值.
    
```
package main
import (
    . "fmt"
)

func Max(a, b int) (int, int) {
    return a+b, a*b
}

func main() {
    x, y := Max(4,5)   //如果调用的函数有多个返回值,接收它的也应该有多个值.
}
```

上面的例子直接返回了两个参数,当然我们也可以命名返回参数的变量。这个例子里面只是用了两个类型,我们也可以改成如下这样的定义,然后返回的时候不用带上变量名,因为直接在函数里面初始化了.
  官方建议: 最好命名返回值,因为不命名返回值,虽然使得代码更加简洁了,但是会造成声称文档可读性差.
  
```
func Max(a, b int) (add int, Multiplied int) {
    add = a + b
    Multiplied = a * b
    return
}
```

### 变参
    Go 函数支持变参.接受变参的函数是有着不定数量的参数的.为了做到这点,首先需要定义函数使其接受变参:
    
```
func myfunc(arg ...int){
    for _, val := range arg {
        println(val)
    }
}

func main() {
    myfunc(1,2,3)
}
```


### 传值与传指针
    当我们传一个参数值到被调用函数里面时,实际上是传了这个值的一份copy,当被调用函数中修改参数值的时候,调用函数中相应实参不会发生任何改变,因为数值变化只作用在copy上.
    
按值传递:

```
package main

func MyFun(a int) int {
    a++
    return a
}

func main() {
    x := 10
    println(x)              //10
    y := MyFun(x)
    println(y)              //11
    println(x)              //10
}
```
在调用MyFun函数时,MyFun接收的参数其实是x的copy,而不是x本身.所以当x的副本值发生改变,x的值并不会发生任何改变.

按址传递:

```
package main

func MyFun(a *int) int {
    *a++
    return *a
}

func main() {
    x := 10
    println(x)             //10
    
    y := MyFun(&x)
    println(y)             //11
    println(x)             //11
}
```
如果是按址传递.变量在内存中存放于一定地址上的,修改变量实际是修改变量地址处的内存.只有MyFun函数知道x变量所在的地址,才能修改x变量的值.所以,我们需要将x所在地址&x传入函数,并将函数的参数的类型由int改为*int,即改为指针类型,才能在函数中修改x变量的值.此时参数仍然是按copy传递的,只是copy的事一个指针.


使用指针优点:
> 指针使得多个函数能操作同一个对象.

> 指针比较轻量级(8bytes),只是穿内存地址,我们可以用指针传递体积大的结构体.如果用参数传递的话,在每次copy上面就会花费相对较多的系统开销(内存和时间).所以当你要传递大的结构体的时候,用指针是一个明智的选择.

> Go 语言中string、slice、map这三种类型的实现机制类似指针,所以可以直接传递.而不用取地址后传递指针.(注: 若函数需要改变slice长度,则仍需要取地址传递指针.)


一个不改变slice长度的实例:
```
package main

import (
    . "fmt"
)

func add(number []int) []int {
    number[0] = 23
    return number
}

func main() {
    number := []int{1, 2, 3}
    Printf("%v\n", number)
    number1 := add(number)
    Printf("%v\n", number1)
    Printf("%v\n", number)    
}

stdout:
[1 2 3]
[23 2 3]
[23 2 3]
```


如果slice的长度发生改变的话,还是使用这种方式就会有问题.所以还是需要将slice的&number传给调用的函数.

```
package main

import (
    . "fmt"
)

func add(number *[]int) []int {
    *number = append(*number, 345)
    return *number
}

func main() {
    number := []int{1, 2, 3}
    Printf("%v\n", number)
    number1 := add(&number)
    Printf("%v\n", number1)
    Printf("%v\n", number)
}

stdout:
[1 2 3]
[1 2 3 345]
[1 2 3 345]
```
