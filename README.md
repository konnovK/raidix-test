# Тестовое задание в RAIDIX (собрать rpm пакет)

## В папке testtask-1.0 хранится исходный код программы.

`$ tree .`

    .
    ├── README.md
    ├── testtask-1.0
    │   ├── Makefile
    │   └── testtask.c
    ├── testtask-1.0-1.el7.x86_64.rpm
    └── testtask.spec

## Для создания rpm пакета сначала соберу этот исходный код в tar:

`$ rm testtask-1.0.tar`
`$ tar czf testtask-1.0.tar testtask-1.0`

*(ключ -c для создания архива)*

*(ключ -z для того чтобы скомпрессировать)*

*(ключ -f для задания файла архива)*

## Теперь перенесу этот tar в папку SOURCES:


`$ rm /home/kk/rpmbuild/SOURCES/testtask-1.0.tar`
`$ cp testtask-1.0.tar /home/kk/rpmbuild/SOURCES/testtask-1.0.tar`


## Теперь перенесу .spec файл в папку SPECS:

`$ rm /home/kk/rpmbuild/SPECS/testtask.spec`
`$ cp testtask.spec /home/kk/rpmbuild/SPECS/testtask.spec`


## Теперь запущу rpmbuild и скормлю ему мой spec файл:

`$ rpmbuild -bb /home/kk/rpmbuild/SPECS/testtask.spec`

*(ключ -bb для cборки бинарного пакета)*

## Скопирую полученный пакет в нашу директорию:
`$ cp /home/kk/rpmbuild/RPMS/x86_64/testtask-1.0-1.el7.x86_64.rpm ./testtask-1.0-1.el7.x86_64.rpm`
