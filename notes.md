# Comments + suggestions

## Value: high, Difficulty: low

* README.md:
  sentence 2: 'that has' -> 'that have'
  sentence 4: 'an the' -> 'the'

* Python has [strong conventions](https://peps.python.org/pep-0008/#package-and-module-names)
  around how modules should be named so you should rename all the `.py` files
  using just lowercase and underscore.

* remove unused imports: numpy and pandas in 1.2, pandas in 2.c and 2.x

* remove unused variables:
  ```
  1.1_Download-IDs(AU).py:
    aDict
  2.a_Matricies\(Standard\).py:
    engine
    period
    release
  2.x_Reclassification_Analysis\(AU\).py:
    engine
    period
    release
  ...
  etc
  ```

## Value: high, Difficulty: medium

* hard-coded dates and filesystem paths in many places - if these scripts are to be
  useful for others then paths and other runtime-specific items should configurable
  somehow, or even parameterized at runtime (e.g. with argparse). For simplicity
  I'd lean towards a config file that you parse with configparser from the
  standard library; see: https://docs.python.org/3/library/configparser.html
  
  Example: create a config file called 'config.ini' with contents:
  ```ini
    [DEFAULT]
    path1 = '/path/to/location/1'
    path2 = '/path/to/location/2'
    datestr1 = '2022-07-18' 
    
    [special]
    path2 = '/path/to/another/location/2'
  ```

  then load it in your script:
    ```python
    import configparser

    config = configparser.ConfigParser()
    config.read('config.ini')

    defaultconf = config['DEFAULT']
    print('default path1 is', defaultconf['path1'])
    print('default path2 is', defaultconf['path2'])
    print('default datestr1 is', defaultconf['datestr1'])

    specialconf = config['special']
    print('special path1 is', specialconf['path1'])
    print('special path2 is', specialconf['path2'])
    ```

* you have no functions def'ed anywhere. Functions help avoid repeated code; keep variable scope
  under control,  and generally make code much easier to read, write and think about. Even scripts
  can (and most should) have functions defined.

* use of python idioms, for example:
  * iterate using `for ... in` instead of intializing, testing then incrementing a counter, e.g.
    use:
    ```
    for a in range(gene_count):
        ...
    ```
    instead of:
    ```
    a = 0
    while a < gene_count:
       ...
       a += 1
    ```
  * test using implicit truth value rather than comparing equality to `True` or `False`, e.g.
    use:
    ```
    if np.isnan(x):
       ...
    if not exists:
       ...
    ```
    instead of:
    ```
    if np.isnan(x) == True:
       ...
    if exists == False:
       ...
  * where possible use string formatting or f-strings to build strings with a variable component,
    e.g.
    ```python
    path = 'https://panelapp.agha.umccr.org/api/v1/panels/?page={page}'
    print(path.format(page=1))
    ```  

## Value: medium-low, Difficulty: easy 

* code style. This is much less important than whether your code works, but consistent style
  is still important to help you and others interpret your code, especially months or years
  after you write it. Python has quite strong code style conventions (see the PEP8 document),
  specifically things like:
  * variables should be all lowercase and underscore, no CamelCase e.g. `exists` not `isExist`
  * lines should be no more than 80 chars long
  * there should be exactly one space between variable and assigned value e.g. `x = 'a'` not
    `x='a'` or `x= 'a'` or any other form.
  * there should be exactly one space after a comma e.g. `print('More Pages =', rerun)` not
    `print('More Pages =',rerun)`
  * consistent use of either single quote ' or double quote " for all strings.
  * comments at the top of modules and scripts should be in the form of a triple-quoted docstring:
    e.g.
    ```python
    """
    This script does a, b and c.

    Author info: ...
    """
    ```
    instead of 
    ```python
    # This script does a, b and c.
    #
    # Author info: ...
    ```
 
## Other

* In script 2.c use calendar.monthrange(yyyy, mm)[1] to get last day in each month;
  you can avoid all the explicit `if month ==` conditions and save yourself a lot of typing.

* query on the hard-coded csrf tokens — what do these do? Is the server handing out the same csrf
  token all the time? 

