U
    ��aw
  �                   @   s�  d dl Zd dlZd dlmZmZ d dlZd dlZd dl	m
Z
 d dlmZmZ e�  ejZejZejZejZejZejZejZdd� ZdZdZeee � eee � eed	 � e d
�Z!dZ"e!d	ks�e!dkr�e"Z#nNze$e!d�Z%e%�&� Z'W n2 e(k
�r   eed � e�)d� e*�  Y nX e'Z#ej+�,e#�Z-de- Z.e�/e.�Z0e0j1dk�r�zde
� Z2e2j3e.dd� e�$d�Z4ee4�Z4ej�5� �6d�Z7e7�8dd�Z7de7�8dd� d Z7e4�9e7� W n" e(k
�r�   eed � Y nX eed e7� need e0j1d� dS )�    N)�Fore�init)�
Html2Image)�Image�
ImageChopsc                 C   sN   t �| j| j| �d��}t�| |�}t�||dd�}|�� }|rJ| �	|�S d S )N)r   r   g       @i����)
r   �new�mode�sizeZgetpixelr   �
difference�addZgetbboxZcrop)�imZbgZdiffZbbox� r   �carbon_now_sh_computer.py�trim   s    r   u  
 █▀▀ ▄▀█ █▀█ █▄▄ █▀█ █▄ █   █▄ █ █▀█ █ █ █   █▀ █ █
 █▄▄ █▀█ █▀▄ █▄█ █▄█ █ ▀█ ▄ █ ▀█ █▄█ ▀▄▀▄▀ ▄ ▄█ █▀█z�----------------------------------------------------
   Share beautiful images of your source code
----------------------------------------------------
 [+] Coded by GH0STH4CKER  [+] www.carbon.now.sh'
� zFile name with extention : z;import requests as r
r.post('www.google.com')
r.status_code� �rz
File not found !�   z�https://carbon.now.sh/embed?bg=rgba%2874%2C144%2C226%2C1%29&t=monokai&wt=none&l=python&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=��   ZHTIscreenshot)ZurlZsave_asz%Y-%m-%d %H:%M:%S�:�-Z	carbonSH_�_z.pngzSaving Failed !z
Image Saved as z
Connection Error (z) !):Zrequestsr   Zurllib.parseZurllibZcoloramar   r   Zdatetime�timeZ
html2imager   ZPILr   r   ZLIGHTYELLOW_EXZCOLylwZYELLOWZCOylwZLIGHTCYAN_EXZCOLcynZLIGHTGREEN_EXZCOLgrnZLIGHTMAGENTA_EXZCOLmgnZLIGHTBLUE_EXZCOLbluZLIGHTRED_EXZCOLredr   ZbigtitleZtagline�print�inputZchoiceZ
samplecode�code�openZfile1�readZLines�	Exception�sleep�exit�parseZ
quote_plus�encodeZcode_url�getZrsZstatus_codeZhtiZ
screenshotr   Znow�strftimeZf_nmdt�replaceZsaver   r   r   r   �<module>   s`   



