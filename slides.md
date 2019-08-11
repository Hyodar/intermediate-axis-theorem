%title: Demonstração do Teorema do Eixo Intermediário usando PyOpenGL
%author: Franco Barpp Gomes
%date: 2019-08-10

-> Introdução <-
================

O trabalho representa uma simulação física do que acontece em um vídeo, "Dancing T-handle in zero-g", disponível no youtube.

Para isso, foi usada a linguagem de scripting **Python** e as seguintes bibliotecas:

* **PyOpenGL** (wrapper da biblioteca original) - renderização 3D
* **FreeGLUT** - adição de algumas funções para OpenGL 
* **PyGame** - controle de eventos e da janela de exibição 
* **NumPy** - processamento numérico

---------------------------------------

-> Pontos importantes <-
========================

Para entender a física por trás desse fenômeno, recomendo o vídeo "Intermediate Axis Theorem - Python Code Included", em que o autor desenvolve uma outra simulação, mas essa usando VPython. (vídeo-exemplo enviado pelo Barreto)

*_Aviso!_* Esse vídeo é ótimo para entender o processo da resolução, mas é  __horrível__ para aprender Python! Tem muitas práticas feias/erradas que poderiam ser facilmente evitadas.

Se não tiver conhecimento prévio em Python, recomendo estudar Python antes para entender o que eu falei sobre o código mostrado no vídeo.
É uma linguagem ótima de aprender, por minha experiência recomendo o SoloLearn Python, mas deve ter muitos materiais abertos ainda melhores.

---------------------------------------

-> Classes e seus usos <-
=========================

Este é o esquema de classes utilizado:

* Axes: representação dos eixos x, y e z
* Cylinder: cilindro com parametros para ser usado como parte da t-bar
* Screen: renderização do menu e do gráfico de momentos angulares
* Tbar: um projeto de t-bar como vista no vídeo, composta por 2 cilindros
* World: configurações e processos de renderização da cena no OpenGL

