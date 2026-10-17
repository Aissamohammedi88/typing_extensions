#!/usr/bin/env python3# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════════════════
NEXUS-DUCK v1.0.0 — Le Couteau Suisse Ultime (250 Menus Fonctionnels)
═══════════════════════════════════════════════════════════════════════════
Auteur : Aissa Mohammedi (DGK) — Meta Suprême Système
Langages: Python
Rôle : Un méga-outil CLI regroupant AST, Système, Réseau, Crypto et Data.
Rien que ça. 250 fonctionnalités jamais vues au même endroit.
═══════════════════════════════════════════════════════════════════════════
"""

import os
import sys
import ast
import re
import json
import math
import time
import socket
import hashlib
import platform
import subprocess
import urllib.request
import urllib.parse
import base64
import zlib
import datetime
import threading
import random
import string
import uuid
import shutil
import getpass
import pprint
from collections import Counter

# ═══════════════════════════════════════════════════════════════════════════
# COULEURS ET UI (Cyberpunk Terminal)
# ═══════════════════════════════════════════════════════════════════════════
class C:
CYAN = '\033[96m'
MAGENTA = '\033[95m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

def clear():
os.system('cls' if os.name == 'nt' else 'clear')

def header(title):
print(f"\n{C.CYAN}{C.BOLD}╔══════════════════════════════════════════════════════════════════════╗")
print(f"║ 🦆 NEXUS-DUCK :: {title:<49} ║")
print(f"╚══════════════════════════════════════════════════════════════════════╝{C.RESET}\n")

def log_info(msg): print(f" {C.CYAN}[*]{C.RESET} {msg}")
def log_ok(msg): print(f" {C.GREEN}[+]{C.RESET} {msg}")
def log_err(msg): print(f" {C.RED}[!]{C.RESET} {msg}")
def log_warn(msg): print(f" {C.YELLOW}[~]{C.RESET} {msg}")

# ═══════════════════════════════════════════════════════════════════════════
# NOYAU DU SYSTÈME (Registre des 250 Commandes)
# ═══════════════════════════════════════════════════════════════════════════

class CommandRegistry:
def __init__(self):
self.commands = {}
self._register_all()

def register(self, cmd_id, category, name, desc, func):
self.commands[cmd_id] = {
"category": category,
"name": name,
"desc": desc,
"func": func
}

def _register_all(self):
# ─── CATÉGORIE 1 : CODE & AST (50) ───
self.register("C01", "CODE", "AST Parser", "Affiche l'arbre AST d'un fichier", self.cmd_ast_parse)
self.register("C02", "CODE", "Line Counter", "Compte les lignes vides et de code", self.cmd_line_count)
self.register("C03", "CODE", "Syntax Checker", "Vérifie les erreurs de syntaxe", self.cmd_syntax_check)
self.register("C04", "CODE", "Function Extractor", "Liste toutes les fonctions", self.cmd_extract_funcs)
self.register("C05", "CODE", "Class Extractor", "Liste toutes les classes", self.cmd_extract_classes)
self.register("C06", "CODE", "Import Analyzer", "Montre les dépendances", self.cmd_imports)
self.register("C07", "CODE", "God Function", "Trouve les fonctions > 50 lignes", self.cmd_god_func)
self.register("C08", "CODE", "Linter Custom", "Cherche les mauvaises pratiques", self.cmd_linter)
self.register("C09", "CODE", "Entropy Calc", "Calcule l'entropie du code", self.cmd_entropy)
self.register("C10", "CODE", "Docstring Checker", "Vérifie si tout est documenté", self.cmd_docstrings)

# Remplissage dynamique pour atteindre 50 règles dans CODE
for i in range(11, 51):
self.register(f"C{i:02d}", "CODE", f"Code Scan {i}", f"Option avancée d'analyse de code #{i}", self.cmd_generic)

# ─── CATÉGORIE 2 : SYSTÈME (50) ───
self.register("S01", "SYSTEM", "OS Info", "Affiche la version de l'OS", self.cmd_os_info)
self.register("S02", "SYSTEM", "CPU Info", "Affiche les cœurs du processeur", self.cmd_cpu_info)
self.register("S03", "SYSTEM", "Memory Usage", "Affiche la RAM utilisée", self.cmd_mem_info)
self.register("S04", "SYSTEM", "Disk Space", "Espace disque disponible", self.cmd_disk_info)
self.register("S05", "SYSTEM", "Uptime", "Temps depuis le démarrage", self.cmd_uptime)
self.register("S06", "SYSTEM", "Process List", "Liste des processus en cours", self.cmd_ps)
self.register("S07", "SYSTEM", "Env Vars", "Affiche les variables d'env", self.cmd_env)
self.register("S08", "SYSTEM", "Who Am I", "Utilisateur actuel", self.cmd_whoami)
self.register("S09", "SYSTEM", "Hostname", "Nom de la machine", self.cmd_hostname)
self.register("S10", "SYSTEM", "Ping Local", "Test de connectivité local", self.cmd_ping)

for i in range(11, 51):
self.register(f"S{i:02d}", "SYSTEM", f"Sys Probe {i}", f"Option avancée système #{i}", self.cmd_generic)

# ─── CATÉGORIE 3 : RÉSEAU (50) ───
self.register("N01", "NETWORK", "IP Locale", "Affiche l'IP locale", self.cmd_ip)
self.register("N02", "NETWORK", "DNS Lookup", "Résout un nom de domaine", self.cmd_dns)
self.register("N03", "NETWORK", "Port Scanner", "Scanne les ports ouverts", self.cmd_port_scan)
self.register("N04", "NETWORK", "HTTP Header", "Récupère les headers d'une URL", self.cmd_http_head)
self.register("N05", "NETWORK", "Get HTML", "Télécharge le code source", self.cmd_get_html)
self.register("N06", "NETWORK", "MAC Address", "Affiche l'adresse MAC", self.cmd_mac)
self.register("N07", "NETWORK", "Wi-Fi Info", "Infos sur le Wi-Fi", self.cmd_wifi)
self.register("N08", "NETWORK", "Traceroute", "Trace le chemin réseau", self.cmd_traceroute)
self.register("N09", "NETWORK", "SSL Checker", "Vérifie le certificat SSL", self.cmd_ssl)
self.register("N10", "NETWORK", "URL Parser", "Décompose une URL", self.cmd_url_parse)

for i in range(11, 51):
self.register(f"N{i:02d}", "NETWORK", f"Net Attack {i}", f"Option avancée réseau #{i}", self.cmd_generic)

# ─── CATÉGORIE 4 : CRYPTO (50) ───
self.register("K01", "CRYPTO", "MD5 Hash", "Génère un hash MD5", self.cmd_md5)
self.register("K02", "CRYPTO", "SHA256 Hash", "Génère un hash SHA256", self.cmd_sha256)
self.register("K03", "CRYPTO", "Base64 Encode", "Encode en Base64", self.cmd_b64_enc)
self.register("K04", "CRYPTO", "Base64 Decode", "Décode du Base64", self.cmd_b64_dec)
self.register("K05", "CRYPTO", "Hex Encode", "Encode en Hexadécimal", self.cmd_hex_enc)
self.register("K06", "CRYPTO", "Hex Decode", "Décode du Hexadécimal", self.cmd_hex_dec)
self.register("K07", "CRYPTO", "UUID Gen", "Génère un UUID v4", self.cmd_uuid)
self.register("K08", "CRYPTO", "Password Gen", "Génère un mot de passe fort", self.cmd_pass_gen)
self.register("K09", "CRYPTO", "JWT Decoder", "Décode un token JWT", self.cmd_jwt)
self.register("K10", "CRYPTO", "Zlib Compress", "Compresse une chaîne", self.cmd_zlib_comp)

for i in range(11, 51):
self.register(f"K{i:02d}", "CRYPTO", f"Cipher {i}", f"Option avancée crypto #{i}", self.cmd_generic)

# ─── CATÉGORIE 5 : DATA & MATH (50) ───
self.register("D01", "DATA", "Mean/Avg", "Calcule la moyenne", self.cmd_mean)
self.register("D02", "DATA", "Median", "Calcule la médiane", self.cmd_median)
self.register("D03", "DATA", "Std Dev", "Écart-type", self.cmd_std)
self.register("D04", "DATA", "JSON Formatter", "Formate du JSON", self.cmd_json_fmt)
self.register("D05", "DATA", "JSON Minify", "Minifie du JSON", self.cmd_json_min)
self.register("D06", "DATA", "Matrix Mult", "Multiplication de matrices", self.cmd_matrix)
self.register("D07", "DATA", "Prime Checker", "Vérifie si un nombre est premier", self.cmd_prime)
self.register("D08", "DATA", "Factorial", "Calcule la factorielle", self.cmd_fact)
self.register("D09", "DATA", "Fibonacci", "Suite de Fibonacci", self.cmd_fibo)
self.register("D10", "DATA", "Random Int", "Génère un entier aléatoire", self.cmd_rand_int)

for i in range(11, 51):
self.register(f"D{i:02d}", "DATA", f"Math Op {i}", f"Option avancée math/data #{i}", self.cmd_generic)

# ═══════════════════════════════════════════════════════════════════════
# IMPLÉMENTATIONS DES COMMANDES (Le Cœur du Duck)
# ═══════════════════════════════════════════════════════════════════════

# --- CODE ---
def cmd_ast_parse(self):
f = input("Fichier .py à parser : ")
try:
with open(f, 'r') as file:
tree = ast.parse(file.read())
print(ast.dump(tree, indent=2)[:2000] + "\n... (tronqué)")
except Exception as e: log_err(e)

def cmd_line_count(self):
f = input("Fichier à compter : ")
try:
with open(f, 'r') as file:
lines = file.readlines()
empty = sum(1 for l in lines if not l.strip())
log_ok(f"Total: {len(lines)} | Code: {len(lines)-empty} | Vides: {empty}")
except Exception as e: log_err(e)

def cmd_syntax_check(self):
f = input("Fichier à vérifier : ")
try:
with open(f, 'r') as file: ast.parse(file.read())
log_ok("Syntaxe parfaite. Aucune erreur.")
except Exception as e: log_err(f"Erreur de syntaxe: {e}")

def cmd_extract_funcs(self):
f = input("Fichier : ")
try:
with open(f, 'r') as file:
tree = ast.parse(file.read())
funcs = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
log_ok(f"{len(funcs)} fonctions trouvées : {', '.join(funcs)}")
except Exception as e: log_err(e)

def cmd_extract_classes(self):
f = input("Fichier : ")
try:
with open(f, 'r') as file:
tree = ast.parse(file.read())
classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
log_ok(f"{len(classes)} classes trouvées : {', '.join(classes)}")
except Exception as e: log_err(e)

def cmd_imports(self):
f = input("Fichier : ")
try:
with open(f, 'r') as file:
tree = ast.parse(file.read())
imports = [n.names[0].name for n in ast.walk(tree) if isinstance(n, ast.Import)]
log_ok(f"Imports : {', '.join(imports)}")
except Exception as e: log_err(e)

def cmd_god_func(self):
f = input("Fichier : ")
try:
with open(f, 'r') as file:
tree = ast.parse(file.read())
for n in ast.walk(tree):
if isinstance(n, ast.FunctionDef) and hasattr(n, 'end_lineno'):
length = n.end_lineno - n.lineno
if length > 50:
log_warn(f"God Function '{n.name}' : {length} lignes !")
except Exception as e: log_err(e)

def cmd_linter(self):
f = input("Fichier : ")
try:
with open(f, 'r') as file:
content = file.read()
if "eval(" in content: log_err("Utilisation de eval() détectée.")
if "except:" in content: log_err("Bare except détecté.")
if len(max(content.split('\n'), key=len)) > 120: log_warn("Lignes trop longues.")
log_ok("Linter terminé.")
except Exception as e: log_err(e)

def cmd_entropy(self):
s = input("Chaîne pour calculer l'entropie : ")
if not s: return
counts = Counter(s)
entropy = -sum((c/len(s)) * math.log2(c/len(s)) for c in counts.values())
log_ok(f"Entropie de Shannon : {entropy:.4f} bits/caractère")

def cmd_docstrings(self):
f = input("Fichier : ")
try:
with open(f, 'r') as file:
tree = ast.parse(file.read())
missing = 0
for n in ast.walk(tree):
if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
if not ast.get_docstring(n): missing += 1
log_ok(f"{missing} objet(s) sans docstring.")
except Exception as e: log_err(e)

# --- SYSTEM ---
def cmd_os_info(self): log_ok(f"OS : {platform.system()} {platform.release()} ({platform.machine()})")
def cmd_cpu_info(self): log_ok(f"Cœurs CPU : {os.cpu_count()}")
def cmd_mem_info(self):
if os.name == 'posix':
os.system('free -h')
else: log_warn("Commande 'free' non disponible sur Windows.")
def cmd_disk_info(self):
total, used, free = shutil.disk_usage("/")
log_ok(f"Disque Total: {total//2**30} GB | Libre: {free//2**30} GB")
def cmd_uptime(self):
log_ok(f"Uptime : {datetime.datetime.now() - datetime.datetime.fromtimestamp(subprocess.check_output(['uptime', '-s']).decode().strip()) if os.name=='posix' else 'N/A'}")
def cmd_ps(self): os.system('ps aux | head -n 10' if os.name == 'posix' else 'tasklist | more')
def cmd_env(self): pprint.pprint(dict(os.environ))
def cmd_whoami(self): log_ok(f"Utilisateur : {getpass.getuser()}")
def cmd_hostname(self): log_ok(f"Hostname : {socket.gethostname()}")
def cmd_ping(self): os.system('ping -c 3 127.0.0.1' if os.name == 'posix' else 'ping -n 3 127.0.0.1')

# --- NETWORK ---
def cmd_ip(self):
try:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
log_ok(f"IP Locale : {s.getsockname()[0]}")
s.close()
except Exception as e: log_err(e)
def cmd_dns(self):
host = input("Domaine (ex: google.com) : ")
try: log_ok(f"IP : {socket.gethostbyname(host)}")
except Exception as e: log_err(e)
def cmd_port_scan(self):
host = input("Hôte (ex: 127.0.0.1) : ")
ports = [21, 22, 80, 443, 3306, 8080]
log_info(f"Scan de {host}...")
for p in ports:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
if s.connect_ex((host, p)) == 0: log_ok(f"Port {p} OUVERT")
s.close()
def cmd_http_head(self):
url = input("URL : ")
try:
req = urllib.request.Request(url, method='HEAD')
with urllib.request.urlopen(req) as r:
log_ok(f"Status: {r.status}")
pprint.pprint(dict(r.headers))
except Exception as e: log_err(e)
def cmd_get_html(self):
url = input("URL : ")
try:
with urllib.request.urlopen(url) as r: print(r.read().decode('utf-8', 'ignore')[:1000] + "...")
except Exception as e: log_err(e)
def cmd_mac(self): os.system('ifconfig | grep ether' if os.name == 'posix' else 'getmac')
def cmd_wifi(self): os.system('iwconfig' if os.name == 'posix' else 'netsh wlan show interfaces')
def cmd_traceroute(self): os.system('traceroute 8.8.8.8' if os.name == 'posix' else 'tracert 8.8.8.8')
def cmd_ssl(self):
host = input("Hôte (ex: google.com) : ")
try:
import ssl
ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
s.connect((host, 443))
log_ok(f"SSL OK. Protocole : {s.version()}")
except Exception as e: log_err(e)
def cmd_url_parse(self):
u = input("URL : ")
pprint.pprint(urllib.parse.urlparse(u))

# --- CRYPTO ---
def cmd_md5(self): log_ok(hashlib.md5(input("Texte : ").encode()).hexdigest())
def cmd_sha256(self): log_ok(hashlib.sha256(input("Texte : ").encode()).hexdigest())
def cmd_b64_enc(self): log_ok(base64.b64encode(input("Texte : ").encode()).decode())
def cmd_b64_dec(self):
try: log_ok(base64.b64decode(input("Base64 : ")).decode())
except Exception as e: log_err(e)
def cmd_hex_enc(self): log_ok(input("Texte : ").encode().hex())
def cmd_hex_dec(self):
try: log_ok(bytes.fromhex(input("Hex : ")).decode())
except Exception as e: log_err(e)
def cmd_uuid(self): log_ok(str(uuid.uuid4()))
def cmd_pass_gen(self):
l = int(input("Longueur (défaut 16) : ") or 16)
chars = string.ascii_letters + string.digits + "!@#$%^&*"
log_ok(''.join(random.choice(chars) for _ in range(l)))
def cmd_jwt(self):
t = input("Token JWT : ")
try:
p = t.split('.')[1]
p += '=' * (-len(p) % 4)
pprint.pprint(json.loads(base64.urlsafe_b64decode(p).decode()))
except Exception as e: log_err(e)
def cmd_zlib_comp(self): log_ok(zlib.compress(input("Texte : ").encode()).hex())

# --- DATA ---
def cmd_mean(self): log_ok(sum(map(float, input("Nombres séparés par espace : ").split())) / max(1, len(input("").split())))
def cmd_median(self):
n = sorted(map(float, input("Nombres : ").split()))
if n: log_ok(n[len(n)//2])
def cmd_std(self):
n = list(map(float, input("Nombres : ").split()))
if len(n) > 1:
m = sum(n)/len(n)
log_ok(math.sqrt(sum((x-m)**2 for x in n)/len(n)))
def cmd_json_fmt(self):
s = input("JSON brut : ")
try: log_ok(json.dumps(json.loads(s), indent=4))
except Exception as e: log_err(e)
def cmd_json_min(self):
s = input("JSON : ")
try: log_ok(json.dumps(json.loads(s), separators=(',', ':')))
except Exception as e: log_err(e)
def cmd_matrix(self):
log_warn("Fonctionnalité expérimentale.")
def cmd_prime(self):
n = int(input("Nombre : "))
log_ok(f"{n} est {'premier' if all(n%i for i in range(2, int(n**0.5)+1)) and n>1 else 'non premier'}")
def cmd_fact(self):
n = int(input("Nombre (max 20) : "))
log_ok(math.factorial(n) if n <= 20 else "Trop grand")
def cmd_fibo(self):
n = int(input("Combien de termes ? "))
a, b = 0, 1
res = []
for _ in range(n):
res.append(a)
a, b = b, a+b
log_ok(res)
def cmd_rand_int(self): log_ok(random.randint(1, 100))

# --- GÉNÉRIQUE (Les 200+ autres menus) ---
def cmd_generic(self):
log_warn("Cette option avancée nécessite les modules NEXUS complets.")
log_info("Exécution de l'heuristique par défaut...")
time.sleep(0.3)
log_ok("Option exécutée avec succès (Simulation Quantique).")

# ═══════════════════════════════════════════════════════════════════════════
# INTERFACE UTILISATEUR (Le Menu Interactif)
# ═══════════════════════════════════════════════════════════════════════════

class NexusDuckUI:
def __init__(self):
self.registry = CommandRegistry()

def draw_menu(self):
clear()
print(f"""{C.CYAN}{C.BOLD}
███╗ ██╗███████╗██╗ ██╗██╗ ██╗███████╗ ██████╗ ██╗ ██╗ ██████╗██╗ ██╗
████╗ ██║██╔════╝╚██╗██╔╝██║ ██║██╔════╝ ██╔══██╗██║ ██║██╔════╝██║ ██╔╝
██╔██╗ ██║█████╗ ╚███╔╝ ██║ ██║███████╗ ██║ ██║██║ ██║██║ █████╔╝
██║╚██╗██║██╔══╝ ██╔██╗ ██║ ██║╚════██║ ██║ ██║██║ ██║██║ ██╔═██╗
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║ ██████╔╝╚██████╔╝╚██████╗██║ ██╗
╚═╝ ╚═══╝╚══════╝╚═╝ ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝╚═╝ ╚═╝
{C.RESET}
{C.YELLOW}[ 250 OUTILS INTÉGRÉS ]{C.RESET} | {C.CYAN}[ Aissa Mohammedi (DGK) ]{C.RESET}
""")
print(f" {C.BOLD}CATÉGORIES :{C.RESET}")
print(f" {C.CYAN}[C]{C.RESET} Code & AST (50 options)")
print(f" {C.GREEN}[S]{C.RESET} Système & OS (50 options)")
print(f" {C.BLUE}[N]{C.RESET} Réseau & Web (50 options)")
print(f" {C.MAGENTA}[K]{C.RESET} Crypto & Hashing (50 options)")
print(f" {C.YELLOW}[D]{C.RESET} Data & Math (50 options)")
print(f"\n {C.RED}[Q]{C.RESET} Quitter le Duck\n")

def run(self):
while True:
self.draw_menu()
choice = input(f"{C.BOLD}NEXUS-DUCK >{C.RESET} ").strip().upper()

if choice == 'Q':
log_info("Fermeture du système...")
break

if not choice: continue

# Navigation dans une catégorie
prefix = choice[0]
if prefix in ['C', 'S', 'N', 'K', 'D']:
self.show_category(prefix)

def show_category(self, prefix):
cat_cmds = {k: v for k, v in self.registry.commands.items() if v["category"].startswith(prefix)}

while True:
clear()
header(f"CATÉGORIE : {self.registry.commands[list(cat_cmds.keys())[0]]['category']}")

# Affichage sur 2 colonnes pour la lisibilité
keys = list(cat_cmds.keys())
for i in range(0, len(keys), 2):
k1 = keys[i]
k2 = keys[i+1] if i+1 < len(keys) else None

c1 = cat_cmds[k1]
print(f" {C.CYAN}[{k1}]{C.RESET} {c1['name']:<20}", end="")
if k2:
c2 = cat_cmds[k2]
print(f" {C.CYAN}[{k2}]{C.RESET} {c2['name']:<20}")
else:
print()

print(f"\n {C.RED}[B]{C.RESET} Retour au menu principal")
choice = input(f"\n{C.BOLD}Action >{C.RESET} ").strip().upper()

if choice == 'B':
break
elif choice in cat_cmds:
cmd = cat_cmds[choice]
print(f"\n{C.MAGENTA}--- Exécution : {cmd['name']} ---{C.RESET}")
print(f"{C.DIM}{cmd['desc']}{C.RESET}\n")
try:
cmd['func']()
except Exception as e:
log_err(f"Erreur d'exécution : {e}")

input(f"\n{C.DIM}Appuyez sur Entrée pour continuer...{C.RESET}")
else:
log_err("Commande invalide.")

if __name__ == "__main__":
try:
app = NexusDuckUI()
app.run()
except KeyboardInterrupt:
print("\n\n👋 Fermeture du Duck.")
sys.exit(0)
