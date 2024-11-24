## 一. 简介

### 1.1 编写目的
​	该脚本旨在提供一个简易的文件管理工具，它的主要功能包括自动化创建目录结构、批量完成文件处理等功能，旨在帮助用户高效地组织文件结构，提高工作效率。

### 1.2 编写背景
​	对于算法工程师来说，查找算法缺陷是一项非常常见的工作，而查找算法缺陷首要的工作就是解析算法日志。在实际应用中，算法日志存在以下特点：

- **分段存储**：即每隔一定时间存一个日志文件；
- **日志共存**：即多个算法的日志按一定顺序或结构共存在同一个文件里，解析时要先找到对应算法的日志部分才好进行下一步操作；
- **多层解析**：在系统复杂时，往往需要多个解析工具对日志进行分层解析，如先系统解析工具解析得到系统的日志，再用算法日志解析工具对解析后的系统日志做进一步的解析，得到算法日志

​	在组合定位任务中的日志即存在以上三个特点，为了将一整段完整数据的日志解析出来，需要以下步骤：1) 将系统日志批量解析得到各个算法的日志；2) 从解析得到的各个算法日志中选出组合定位日志对应的文件，移动至单独的文件夹中；3) 对组合定位日志批量解析，得到组合定位日志；4) 对解析后的日志按时间进行合并，获得完整的日志。以上这些操作如果没有批量的自动化的工具，则只能通过手动复制粘贴的方式，不仅费时费力，且容易出错。

​	在此背景下，本文开发了自动化的工具，实现了常见操作的自动化处理，可以显著的提高工作效率。

### 1.3 术语缩写
- `src`: 源文件夹 (source)
- `dst`: 目标文件夹 (destination)
- `file`: 文件 (file)

### 1.4 参考资料
- [Python官方文档](https://docs.python.org/3/)

## 二. 工具使用说明

### 2.1 创建文件结构

**函数说明**：

该函数支持根据字典结构创建文件夹和文件。

**函数接口**：

```python
def create_directory_structure(parent_folder: str, structure: dict) -> None:
```

**参数说明**：
- `parent_folder`: 父文件夹路径
- `structure`: 文件夹和文件结构，字典类型，键为文件夹名，值为文件名或子文件夹名或子文件夹字典

**调用示例**：

```python
structure = {


**调用示例**：
```python
structure = {
    "project": {
        "README.md": "项目文档",
        "data": {
            "data1.txt": "数据文件一",
            "data2.txt": "数据文件二"
        }
    }
}
create_directory_structure('/path/to/parent', structure)
```

### 2.2 复制或移动文件
**函数说明**：
    
该函数支持按照正则表达式匹配模式，将源文件夹中的文件复制或移动到目标文件夹中。

**函数接口**：

```python
def move_files(source_folder: str, target_folder: str, pattern: str = None, copy_files: bool = False) -> None:
```

**参数说明**：
- `source_folder`: 源文件夹路径
- `target_folder`: 目标文件夹路径
- `pattern`: 匹配模式，默认为None，表示全部文件
- `copy_files`: 是否复制文件，默认为False，表示移动文件

**调用示例**：

```python
# move file
move_files(source_folder=base_directory, target_folder=base_directory + "raw", pattern=r"\.bin")
```

### 2.3 合并文件
**函数说明**：

该函数支持按照时间顺序合并多个文件。

**函数接口**：

```python
def merge_files(source_folder: str, target_file: str, pattern: str = None) -> None:
```

**参数说明**：
- `source_folder`: 源文件夹路径
- `target_file`: 目标文件路径
- `pattern`: 匹配模式，默认为None，表示全部文件


**调用示例**：

```python
# merge files
merge_files(source_folder=base_directory, target_file=base_directory + "log/all_log.txt", pattern=r"log.*\.txt")
```

## 三. 环境依赖
- Python 3.6+
- 第三方库：
    - `re`：正则表达式匹配
    - `os`：文件系统操作
- 系统依赖：
    - 无

## 四. 版本更新
- 2024.11.24：V1.0.0