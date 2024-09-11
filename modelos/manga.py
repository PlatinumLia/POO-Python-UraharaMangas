class Manga:
    nome = "";
    volumes = "";
    ativo = False;
    
manga_bleach = Manga();
manga_blackclover = Manga();

manga_bleach.nome = "Bleach";
manga_blackclover = "Black Clover";

mangas = [manga_bleach, manga_blackclover];

print(mangas)
print(manga_bleach)
print(dir(manga_bleach))