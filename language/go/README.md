# GO

[TOC]

简要：

>数据类型：
>
>计算机用来计算，计算前需要存数，如何存数
>
>数据类型作用：
>
>告诉编译器这个数（变量）应该占用多大的内存空间

 ![](/home/westwell/Pictures/golang.png)

 



# 基础知识

go 语言关键字、标识符、数据类型、变量、流程控制、函数、数组、闭包

## 关键字

break - 使用break关键字可以终止循环并继续执行其余代码
case - 这是switch构造的一种形式。我们在切换后指定一个变量。
chan - chan 关键字用于定义通道。在执行中，允许您同时运行并行代码。
const - const关键字用于标量值引入名称，常量
continue - continue使用关键字可以返回到for循环的开头，跳过当前循环
default - default语句是可选的，在switch语句中使用case和default.如果值与表达式不匹配，则跳到默认值。
defer - 关键字defer用于推迟执行功能，直到周围的功能执行为止，如果是在函数中最后执行
else - 如果if条件为假，则执行else下的语句
fallthrough - 在switch语句中使用该关键字。当我们使用该关键字时，将执行下面的case条件
for - for开始for循环
func - func关键字声明一个函数
go - go关键字触发一个goroutine(异步处理)，该例程由golang运行时管理
goto - goto关键字可无条件跳转至带标签的语句
if - if语句用于检查循环内的特定条件。
import - import 关键字用于导入软件包。
interface - interface关键字用于指定方法集。方法集时一种类型的方法列表。
map - map关键字定义map类型。映射是键值对的无序集合。
package - package关键字代码在包中分组为一个单元。类似代码文件在文件夹中的统一包名。
range - range关键字可以迭代列表(map或者数组)。遍历循环(map或者数组)。
return - go允许您将返回值用作变量，并且可以为此目的使用return关键字。
select - select关键字使goroutine在同步通信操作期间等待处理。
struct - struct是字段的集合。我们可以在字段声明后使用struct关键字，定义结构体。
switch - switch语句用于启动循环并在块内使用if-else逻辑。
type - type我们可以使用type关键字引入新的结构类型。
var - var关键字用于创建go语言的变量

## 标识符

标识符是指go语言对各种函数、方法、变量等命名时使用的字符序列，标识符由若干个字母、下划线_、和数字组成，并且第一个字符必须是字母。 下划线_是一个特殊的标识符，称之为空白标识符，它可以像其他标识符那样用于变量的声明或赋值(任何类型都可以赋值给它),它赋值给它的值都将被抛弃，因此不可以使用_作为变量给其他变量进行赋值或运算。 变量、类型、函数或者代码内标识符的名称不能重复。

标识符命名需要遵守以下规则：
由 26个字母、0-9、_组成
不能以数字开头，必须以字母
go 语言中严格区分大小写
标识符不能包含空格
不能以系统关键字作为标识符，比如：break、if等
命名标识符还需要注意以下几点：
标识符命名尽量简短并且有意义，让人容易理解
不能和标准库中的包名重复
为变量、函数、常量命名时采用驼峰命名法，例如 stuName、getVal

## 数据类型

bool - 布尔型的值只可以是常量 true 或者 false。一个简单的例子：var b bool = true。 数字类型 - 整型 int 和浮点型 float32、float64，Go 语言支持整型和浮点型数字，并且支持复数，其中位的运算采用补码。 字符串类型 - string 错误类型 派生类型: - 指针类型 pointer - 数组类型 - 结构化类型 struct - 通道类型 channel - 函数类型 - 切片类型 - 接口类型 interface - map类型

## 指针类型

类型指针：允许对这个指针类型的数据进行修改，传递数据可以直接使用指针，而无须拷贝数据，类型指针不能进行偏移和运算。

切片指针：由指向起始元素的原始指针、元素数量和容量组成。 （变量、指针和地址三者的关系是：每个变量都拥有地址，指针的值就是地址）

变量、指针地址、指针变量、取地址、取值的相互关系和特性如下：

对变量进行取地址操作使用&操作符，可以获得这个变量的指针变量。
指针变量的值是指针地址。
对指针变量进行取值操作使用*操作符，可以获得指针变量指向的原变量的值。
*操作符作为右值时，意义是取指针的值，作为左值时，也就是放在赋值操作符的左边时，表示 a 指针指向的变量。其实归纳起来，*操作符的根本意义就是操作指针指向的变量。当操作在右值时，就是取指向变量的值，当操作在左值时，就是将值设置给指向的变量。

## 数组类型

数组被称为array,就是一个由若干相同类型的元素组成的序列。 注意：数组的长度是数组类型的一部分。只要类型声明中数组长度不同，即使两个数组类型的元素类型相同，它们还是不同的类型。列入：[2]string和[3]string 数组类型的下标都是整数

### 结构化类型 struct

基础数据类型可以表示一些事物的基本属性，但是当我们想表达一个事物所有或者部分的属性时，go语言提供了一种自定义的数据类型，可以封装多个基础数据类型，这种数据类型叫做结构体。struct

### 通道类型 channel

通道channel是一种特殊的类型 在任何时候，同时只能有一个goroutine访问通道进行发送和获取数据。goroutine之间通过通道就可以通信。

通道像一个传送带或者队列，总是遵循先进先出的规则，保证收发数据的顺序。

channel本身就是一个队列，先进先出
线程安全，不需要加锁
本身是有类型的，string、int等，如果要存多种类型，则定义成interface类型
channel是引用类型，必须make之后才能使用，一旦make，它的容量就确定了，不会动态增加！！！它和map,slice不一样

#### 特点：

一旦初始化容量，就不会改变了
当写入数据容量已满时，不可再写入，取空时，不可以取。
发送将持续阻塞直到数据被接受
把数据往通道中发送时，如果接收方一直没有接收，那么发送操作将持续阻塞。

接收将持续阻塞直到发送方发送数据
如果接收方接收时，通道中没有发送方发送的数据，接收方也会发送阻塞，直到发送方发送数据为止

每次接收一个元素
通道一次只能接收一个元素。

## 函数类型

可以把函数作为一种变量，用type去定义它，那么这个函数类型就可以作为值传递 type calsulTest func(int,int) //声明一个函数类型

### 切片类型

数据结构是切片，动态数组，其长度并不固定，可以在切片中追加元素，它会在容量不足时自动扩容。 切片长度可以随着元素数量的增长而增长（但不会随着元素的数量减少而减少） 切片数据类型是有如下结构体表示的 - Data 是指向数组的指针 - Len 是当前切片的长度 - Cap 是当前切片的容量大小，即Data数组的大小 切片占用的内存空间=切片中元素大小 X 切片容量 切片自动扩容，扩容后新切片的容量将会是原切片容量的2倍，如果还是不足以容纳新元素，则按照同样的操作继续扩容，直到新容量不小于原长度与追加的元素数量之和。 切片扩容是生成容量更大的切片，把原有元素和新元素一并copy到新切片中。

### 接口类型 interface

interface是一种类型，从它的定义可以看出用了type关键字，准确的来说interface是一种具有一组方法的类型. interface被多种类型实现时，需要区分interface的变量时那种储存类型的值，go需要用断言方式。go 可以使用 comma, ok 的形式做区分 value, ok := em.(T)：em 是 interface 类型的变量，T代表要断言的类型，value 是 interface 变量存储的值，ok 是 bool 类型表示是否为该断言的类型 T。

### map类型

map是一堆键值对的未排序集合，类似Python中字典的概念，它的格式为map[keyType]valueType，是一个key-value的hash结构。map的读取和设置也类似slice一样，通过key来操作，只是slice的index只能是int类型，而map多了很多类型，可以是int，可以是string及所有完全定义了==与!=操作的类型。

map 声明 (其中：key为键类型，value为值类型)
var map变量名 map[key] value

#### 注意事项

map是无序的，每次打印出来的map都会不一样，它不能通过index获取，而必须通过key获取。
map的长度是不固定的，也就是和slice一样，也是一种引用类型。
内置的len函数同样适用于map，返回map拥有的key的数量。
map的值可以很方便的修改，通过重新赋值即可。
关键字: map make delete

## 变量

var 声明语句可以创建一个特定类型的变量，然后给变量附加名称，并且设置初始值

 var 变量名称 类型 = 表达式
 var aa string = "golang"
简洁声明 :

 aa := "golang"
初始化一组变量

 i,j := 0,1
注意
:=是一个变量声明语句
=是一个变量赋值操作
指针

一个变量对应一个保存了变量对应类型值的内存空间。普通变量在声明语句创建时被绑定到一个变量名，比如叫x的变量，但是还有很多变量始终以表达式方式引入，例如x[i]或者x.f变量。所有这些表达式一般都是读取一个变量的值，除非它们是出现在赋值语句的左边，这种时候是给对应变量赋予一个新的值。

一个指针的值是另外一个变量的地址。一个指针对应变量在内存中的储存位置。并不是每一个值都会有一个内存地址，但是对于每一个变量必然有对应的内存地址。

如果用“var x int”声明语句声明一个x变量，那么&x表达式（取x变量的内存地址）将产生一个指向该整数变量的指针，指针对应的数据类型是int，指针被称之为“指向int类型的指针”。如果指针名字为p，那么可以说“p指针指向变量x”，或者说“p指针保存了x变量的内存地址”。同时p表达式对应p指针指向的变量的值。一般p表达式读取指针指向的变量的值，这里为int类型的值，同时因为p对应一个变量，所以该表达式也可以出现在赋值语句的左边，表示更新指针所指向的变量的值。

p := &x         // p, of type *int, points to x
fmt.Println(*p) // "1"
*p = 2          // equivalent to x = 2
fmt.Println(x)  // "2"
任何类型的指针的零值都是nil.如果p指向某个有效变量，那么p != nil测试为真。指针之间也是可以进行相等测试的，只有当它们指向同一个变量或全部是nil时才相等。

var x, y int
fmt.Println(&x == &x, &x == &y, &x == nil) // "true false false"

## 流程控制

### if else (分支结构)

关键字 if 是用于测试某个条件（布尔型或逻辑型）的语句，如果该条件成立，则会执行 if 后由大括号{}括起来的代码块，否则就忽略该代码块继续执行后续的代码。如果存在第二个分支，则可以在上面代码的基础上添加 else 关键字以及另一代码块，这个代码块中的代码只有在条件不满足时才会执行，if 和 else 后的两个代码块是相互独立的分支，只能执行其中一个。

if condition {
    // do something
} else {
    // do something
}

### for (循环结构)

与多数语言不同的是，Go语言中的循环语句只支持 for 关键字，而不支持 while 和 do-while 结构，关键字 for 的基本使用方法与C语言和 C++ 中非常接近：

sum := 0
for i := 0; i < 10; i++ {
    sum += i
}
for 中的结束语句——每次循环结束时执行的语句 在结束每次循环前执行的语句，如果循环被 break、goto、return、panic 等语句强制退出，结束语句不会被执行。

### for range (键值循环)

for range 结构是Go语言特有的一种的迭代结构，在许多情况下都非常有用，for range 可以遍历数组、切片、字符串、map 及通道（channel），for range 语法上类似于其它语言中的 foreach 语句，一般形式为：

for key, val := range coll {
   fmt.Println(key,val)
}
通过 for range 遍历的返回值有一定的规律：

数组、切片、字符串返回索引和值。
map 返回键和值。
通道（channel）只返回通道内的值。
switch case 语句

switch 的语法设计，case 与 case 之间是独立的代码块，不需要通过 break 语句跳出当前 case 代码块以避免执行到下一行，示例代码如下：

var a = "hello"
switch a {
case "hello":
    fmt.Println(1) // 输出 1
case "world":
    fmt.Println(2)
default:
    fmt.Println(0)
}
一分支多值 (多个条件对应一个值)

var a = "mum"
switch a {
case "mum", "daddy":
    fmt.Println("family")
}
分支表达式

var r int = 11
switch {
case r > 10 && r < 20:
    fmt.Println(r)
}
跨越 case 的 fallthrough——兼容C语言的 case 设计

在Go语言中 case 是一个独立的代码块，执行完毕后不会像C语言那样紧接着执行下一个 case，但是为了兼容一些移植代码，依然加入了 fallthrough 关键字来实现这一功能

var s = "hello"
switch {
case s == "hello":
    fmt.Println("hello")
    fallthrough
case s != "world":
    fmt.Println("world")
}
// 输出 hello world
goto语句——跳转到指定的标签

goto 语句通过标签进行代码间的无条件跳转，同时 goto 语句在快速跳出循环、避免重复退出上也有一定的帮助，使用 goto 语句能简化一些代码的实现过程。

package main
import "fmt"
func main() {
    for x := 0; x < 10; x++ {
        for y := 0; y < 10; y++ {
            if y == 2 {
                // 跳转到标签
                goto breakHere
            }
        }
    }
    // 手动返回, 避免执行进入标签
    return
    // 标签
breakHere:
    fmt.Println("done")
}
// 标签只能被 goto 使用，但不影响代码执行流程，此处如果不手动返回，在不满足条件时，也会执行第 24 行代码。
// 输出 y=2时候跳到标签breakHere,输出done
// 使用场景:打印日志等

## 函数

函数的基本组成为：关键字 func、函数名、参数列表、返回值、函数体和返回语句，每一个程序都包含很多的函数，函数是基本的代码块。 当函数执行到代码块最后一行}之前或者 return 语句的时候会退出，其中 return 语句可以带有零个或多个参数，这些参数将作为返回值供调用者使用，简单的 return 语句也可以用来结束 for 的死循环，或者结束一个协程（goroutine）。

三种类型的函数：

普通的带有名字的函数
匿名函数或者 lambda 函数
方法
普通函数声明（定义）

函数声明包括函数名、形式参数列表、返回值列表（可省略）以及函数体。

func aa(a int) int {
    return a
}
fmt.Println(aa(123)) // 123
//
func 函数名(形式参数列表)(返回值列表){
    函数体
}
函数变量——把函数作为值保存到变量中

函数也是一种类型，可以和其他类型一样保存在变量中，下面的代码定义了一个函数变量 f，并将一个函数名为 fire() 的函数赋给函数变量 f，这样调用函数变量 f 时，实际调用的就是 fire() 函数

package main
import (
    "fmt"
)
func fire() {
    fmt.Println("fire")
}
func main() {
    var f func()
    f = fire
    f()
}
// 输出 fire
package main
import (
    "fmt"
)
func fire() int {
    return 24
}
func main() {
    f := func() int { return 0 }
    f = fire
    fmt.Println(f())
}
// 输出 24
// 函数变量 f 进行函数调用，实际调用的是 fire() 函数。
匿名函数

匿名函数是指不需要定义函数名的一种函数实现方式，由一个不带函数名的函数声明和函数体组成。

定义一个匿名函数
f := func(aa int) {
    fmt.Println(aa)
    return
}
// 使用f()调用
f(24)
// 输出 24 
匿名函数的用途非常广泛，它本身就是一种值，可以方便地保存在各种容器中实现回调函数和操作封装。

匿名函数用作回调函数
package main
import (
    "fmt"
)
// 遍历切片的每个元素, 通过给定函数进行元素访问
func visit(list []int, f func(int)) {
    for _, v := range list {
        f(v)
    }
}
func main() {
    // 使用匿名函数打印切片内容
    visit([]int{1, 2, 3, 4}, func(v int) {
        fmt.Println(v)
    })
}
// 输出 1 2 3 4
// 使用 visit() 函数将整个遍历过程进行封装，当要获取遍历期间的切片值时，只需要给 visit() 传入一个回调参数即可。

defer（延迟执行语句）

defer 语句会将其后面跟随的语句进行延迟处理，在 defer 归属的函数即将返回时，将延迟处理的语句按 defer 的逆序进行执行，也就是说，先被 defer 的语句最后被执行，最后被 defer 的语句，最先被执行。 逆序执行（类似栈，即后进先出）

package main
import (
    "fmt"
)
func main() {
    fmt.Println("defer begin")
    // 将defer放入延迟调用栈
    defer fmt.Println(1)
    defer fmt.Println(2)
    // 最后一个放入, 位于栈顶, 最先调用
    defer fmt.Println(3)
    fmt.Println("defer end")
}
// 输出 
// defer begin
// defer end
// 3
// 2
// 1

代码的延迟顺序与最终的执行顺序是反向的
延迟调用是在 defer 所在函数结束时进行，函数结束可以是正常返回时，也可以是发生宕机时。
使用延迟执行语句在函数退出时释放资源

处理业务或逻辑中涉及成对的操作是一件比较烦琐的事情，比如打开和关闭文件、接收请求和回复请求、加锁和解锁等。在这些操作中，最容易忽略的就是在每个函数退出处正确地释放和关闭资源。 defer 语句正好是在函数退出时执行的语句，所以使用 defer 能非常方便地处理资源释放问题。

使用延迟并发解锁

函数中并发使用 map，为防止竞态问题，使用 sync.Mutex 进行加锁

var (
    // 一个演示用的映射
    valueByKey      = make(map[string]int)
    // 保证使用映射时的并发安全的互斥锁
    valueByKeyGuard sync.Mutex
)
// 根据键读取值
func readValue(key string) int {
    // 对共享资源加锁
    valueByKeyGuard.Lock()
    // 取值
    v := valueByKey[key]
    // 对共享资源解锁
    valueByKeyGuard.Unlock()
    // 返回值
    return v
}
// 实例化一个 map，键是 string 类型，值为 int。
// map 默认不是并发安全的，准备一个 sync.Mutex 互斥量保护 map 的访问。
// readValue() 函数给定一个键，从 map 中获得值后返回，该函数会在并发环境中使用，需要保证并发安全。
// 使用互斥量加锁。
// 从 map 中获取值。
// 使用互斥量解锁。
// 返回获取到的 map 值。

使用 defer 语句对上面的语句进行简化

func readValue(key string) int {
    valueByKeyGuard.Lock()

    // defer后面的语句不会马上调用, 而是延迟到函数结束时调用
    defer valueByKeyGuard.Unlock()
    return valueByKey[key]
}
使用延迟释放文件句柄

文件的操作需要经过打开文件、获取和操作文件资源、关闭资源几个过程，如果在操作完毕后不关闭文件资源，进程将一直无法释放文件资源

func fileSize(filename string) int64 {
    f, err := os.Open(filename)
    if err != nil {
        return 0
    }
    // 延迟调用Close, 此时Close不会被调用
    // 注意，不能将这一句代码放在第 4 行空行处(err 上方/open打开文件下方)，一旦文件打开错误，f 将为空，在延迟语句触发时，将触发宕机错误。
    defer f.Close()
    info, err := f.Stat()
    if err != nil {
        // defer机制触发, 调用Close关闭文件
        return 0
    }
    size := info.Size()
    // defer机制触发, 调用Close关闭文件
    return size
}

## 递归函数

所谓递归函数指的是在函数内部调用函数自身的函数。

构成递归需要具备以下条件：

一个问题可以被拆分成多个子问题
拆分前的原问题与拆分后的子问题除了数据规模不同，但处理问题的思路是一样的
不能无限制的调用本身，子问题需要有退出递归状态的条件
注意：编写递归函数时，一定要有终止条件，否则就会无限调用下去，直到内存溢出。

宕机（panic）——程序终止运行

系统会在编译时捕获很多错误，但有些错误只能在运行时检查，如数组访问越界、空指针引用等，这些运行时错误会引起宕机。 宕机不是一件很好的事情，可能造成体验停止、服务中断，就像没有人希望在取钱时遇到 ATM 机蓝屏一样，但是，如果在损失发生时，程序没有因为宕机而停止，那么用户将会付出更大的代价，这种代价可以是金钱、时间甚至生命，因此，宕机有时也是一种合理的止损方法。 当宕机发生时，程序会中断运行，并立即执行在该 goroutine（可以先理解成线程）中被延迟的函数（defer 机制），随后，程序崩溃并输出日志信息，日志信息包括 panic value 和函数调用的堆栈跟踪信息，panic value 通常是某种错误信息。

手动触发宕机
package main
func main() {
    panic("crash")
}
在宕机时触发延迟执行语句
当 panic() 触发的宕机发生时，panic() 后面的代码将不会被运行，但是在 panic() 函数前面已经运行过的 defer 语句依然会在宕机发生时发生作用.

package main
import "fmt"
func main() {
    defer fmt.Println("宕机后要做的事情1")
    defer fmt.Println("宕机后要做的事情2")
    panic("宕机")
}
// 输出
// 宕机后要做的事情2
// 宕机后要做的事情1
// 宕机
宕机前，defer 语句会被优先执行

宕机恢复（recover）——防止程序崩溃

Recover 是一个Go语言的内建函数，可以让进入宕机流程中的 goroutine 恢复过来，recover 仅在延迟函数 defer 中有效，在正常的执行过程中，调用 recover 会返回 nil 并且没有其他任何效果，如果当前的 goroutine 陷入恐慌，调用 recover 可以捕获到 panic 的输入值，并且恢复正常的执行。

panic 和 recover 的关系,panic 和 recover 的组合有如下特性：

有 panic 没 recover，程序宕机。
有 panic 也有 recover，程序不会宕机，执行完对应的 defer 后，从宕机点退出当前函数后继续执行。
Test功能测试函数

完善的测试体系，能够提高开发的效率，当项目足够复杂的时候，想要保证尽可能的减少 bug，有两种有效的方式分别是代码审核和测试，Go语言中提供了 testing 包来实现单元测试功能。 要开始一个单元测试，需要准备一个 go 源码文件，在命名文件时文件名必须以_test.go结尾，单元测试源码文件可以由多个测试用例（可以理解为函数）组成，每个测试用例的名称需要以 Test 为前缀，例如：

func TestXxx( t *testing.T ){
    //......
}
编写测试用例有以下几点需要注意：

测试用例文件不会参与正常源码的编译，不会被包含到可执行文件中
测试用例的文件名必须以_test.go结尾
需要使用 import 导入 testing 包
测试函数的名称要以Test或Benchmark开头，后面可以跟任意字母组成的字符串，但第一个字母必须大写，例如 TestAbc()，一个测试用例文件中可以包含多个测试函数
单元测试则以(t *testing.T)作为参数，性能测试以(t *testing.B)做为参数
测试用例文件使用go test命令来执行，源码中不需要 main() 函数作为入口，所有以_test.go结尾的源码文件内以Test开头的函数都会自动执行。
testing 包提供了三种测试方式，分别是单元（功能）测试、性能（压力）测试和覆盖率测试。

单元（功能）测试
性能（压力）测试
覆盖率测试
