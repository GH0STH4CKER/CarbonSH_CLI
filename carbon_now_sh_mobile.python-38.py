U
    �
a?  �                   @   s�  d dl Zd dlZd dlmZmZ d dlZd dlZd dl	m
Z
 d dlmZmZ e�  ejZejZejZejZejZejZejZdZdZeee � eee � eed � dd	� Ze d
�Z!dZ"e!dks�e!dkr�e"Z#nNze$e!d�Z%e%�&� Z'W n2 e(k
�r   eed � e�)d� e*�  Y nX e'Z#ej+�,e#�Z-de- Z.e�/e.�Z0e0j1dk�rzdZ2de2 d d e. Z3e
� Z4e4�/e3�Z5e4�/e3�Z5e5j6�7�  e5j1Z8ej�9� �:d�Z;e;�<dd�Z;de;�<dd� d Z;e8dk�rhzne$dd�Z=e=�>e5j?� e=�@�  e�$d�ZAeeA�ZAej�9� �:d�ZBeB�<dd�ZBdeB�<dd� d ZBeA�CeB� W n" e(k
�rV   eed � Y nX eed e;� need  e8d!� need" e0j1d!� dS )#�    N)�Fore�init)�HTMLSession)�Image�
ImageChopsu  
 █▀▀ ▄▀█ █▀█ █▄▄ █▀█ █▄ █   █▄ █ █▀█ █ █ █   █▀ █ █
 █▄▄ █▀█ █▀▄ █▄█ █▄█ █ ▀█ ▄ █ ▀█ █▄█ ▀▄▀▄▀ ▄ ▄█ █▀█z�----------------------------------------------------
   Share beautiful images of your source code
----------------------------------------------------
 [+] Coded by GH0STH4CKER  [+] www.carbon.now.sh
� c                 C   sN   t �| j| j| �d��}t�| |�}t�||dd�}|�� }|rJ| �	|�S d S )N)r   r   g       @i����)
r   �new�mode�sizeZgetpixelr   �
difference�addZgetbboxZcrop)�imZbgZdiffZbbox� r   �carbon_now_sh_mobile.py�trim   s    r   zFile name with extention : z;import requests as r
r.post('www.google.com')
r.status_code� �rz
File not found !�   z�https://carbon.now.sh/embed?bg=rgba%2874%2C144%2C226%2C1%29&t=monokai&wt=none&l=python&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=��   z&53402-cfa7d4076721b0d496bc40187d9c5954zhttp://image.thum.io/get/auth/z/width/1366�/z%Y-%m-%d %H:%M:%S�:�-Z	carbonSH_�_z.pngz
THUMIO.png�wbz
Error occured while saving !z
Success !
Image Saved as z
Convert Error (z) !z
Connection Error ()DZrequestsr   Zurllib.parseZurllibZcoloramar   r   Zdatetime�timeZrequests_htmlr   ZPILr   r   ZLIGHTYELLOW_EXZCOLylwZYELLOWZCOylwZLIGHTCYAN_EXZCOLcynZLIGHTGREEN_EXZCOLgrnZLIGHTMAGENTA_EXZCOLmgnZLIGHTBLUE_EXZCOLbluZLIGHTRED_EXZCOLredZbigtitleZtagline�printr   �inputZchoiceZ
samplecode�code�openZfile1�readZLines�	Exception�sleep�exit�parseZ
quote_plus�encodeZcode_url�getZrsZstatus_codeZauthZimgUrl�s�resZhtmlZrenderZrcZnow�strftimeZf_date�replace�file�writeZcontent�closer   Zf_nmdtZsaver   r   r   r   �<module>   sz   








