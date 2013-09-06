Computação Científica Com Python
============================

Material do mini-curso de "Computação Científica com Python" (Only portuguese).

## Instalação dos módulos
### Linux (testado no Ubuntu 13.04)
* sudo apt-get install python-numpy python-scipy python-matplotlib python-imaging python-pip
* sudo apt-get build-dep python-scipy
* sudo pip install scikit-learn
* sudo pip install scikit-image
### Windows
* [python](http://www.python.org/download/releases/2.6/ "python")
    1. Recomendo baixar a versão 2.6. É necessários baixar os pacotes (abaixo) de acordo com a versão do python instalada.
    2. Execute o instalador, configure a variável de ambiente da seguinte maneira:
        1. Botão direito do mouse em cima de "Meu computador", clique na aba "Avançado" e em seguida no botão "Variáveis de ambiente".
        2. Em variáveis do sistema, clique no botão "Nova" em "Nome da variável" preencha **PYTHONPATH** e em "Valor da variável" **C:\Python26;C:\Python26\Lib\site-packages;C:\Python26\Lib\;**
        3. Na variável Path, adicione: **,%PYTHONPATH%**
        4. Para testar abra o DOS e digite: python
* [Visual C++ Express](http://download.microsoft.com/download/A/5/4/A54BADB6-9C3F-478D-8657-93B3FC9FE62D/vcsetup.exe "Visual C++") (para compilar o scikit-learn e scikit-image)
* [numpy](http://sourceforge.net/projects/numpy/files/NumPy/ "numpy")
* [scipy](http://sourceforge.net/projects/scipy/files/scipy/ "scipy")
* [matplotlib](http://matplotlib.org/downloads.html "matplotlib")
* [python-imaging](http://www.pythonware.com/products/pil/ "python-imaging")
* [python-setuptools](http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools "python-setuptools")
* [python-pip](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip "python-pip")
* pip install scikit-learn
    * É necessário executar o comando do prompt de comando do visual c++
* pip install scikit-image
    * É necessário executar o comando do prompt de comando do visual c++
