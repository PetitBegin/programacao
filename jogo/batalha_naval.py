from random import randint

bombs = []
for i in range(9):
    x, y = [randint(0,4) for _ in range(2)]
    bombs.append((x,y))

bomba = "💣"
agua = "🌊"

tabuleiro = [
   [ "🟦", "🟦", "🟦","🟦", "🟦"],
   [ "🟦", "🟦", "🟦","🟦", "🟦"],  
   [ "🟦", "🟦", "🟦","🟦", "🟦"],
   [ "🟦", "🟦", "🟦","🟦", "🟦"],
   [ "🟦", "🟦", "🟦","🟦", "🟦"],
   
   ]
while true:
    opcao: str = str(input("Você deseja continuar jogando?( se sim: digite S e se não que mais jogar, digite N )", ))
    if opcao =