# 案例描述
- 公司今天招聘了10个员工（ABCDEFGHIJK）, 10名员工进入公司以后，需要指派员工在哪个部门工作
- 员工信息有： 姓名 工资组成； 部门分为: 策划、美术、研发
- 随机给10名员工分配部门和工资
- 通过multimap 进行信息的插入 key(部门编号) value(员工)
- 分部门显示员工信息

# 实现步骤
1. 创建10个员工，方法哦vector中
2. 遍历vector容器，取出每个员工，进行随机分组
3. 分组后，将员工部门编号作为key，具体员工做为value,放入到multimap容器中
4. 分部门显示员工信息