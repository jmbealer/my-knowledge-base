---
title: Test PlantUML
author: Justin Bealer
date_created: 2023-03-03, 06-20-08
date_modified: 2024-09-18, 06-46-21
reference: 
description: 
aliases: 
tags: 
---
# testingPlantuml

``` plantuml
@startmindmap
+ Computer Science

+ Pick a Language

++ Python
++ Go
++ C#
++ Rust

-- C++
-- C
-- Java
@endmindmap
```

``` plantuml
@startmindmap
+ root
**:right_1.1
right_1.2;
++ right_2

left side

-- left_1
-- left_2
**:left_3.1
left_3.2;

++ roott
@endmindmap
```

``` plantuml
@startuml
' this is a comment
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
John --> Alice: another Authentication Request
Alice --> John: another Authentication Response
@enduml
```

![](file:///tmp/babel-KhZtLB/plantuml-ICaVOY.png)

./test.png

![](./test.png)

<span class="spurious-link" target="test.png">*test.png*</span>

![](img:./test.png) ![](img:test.png)
