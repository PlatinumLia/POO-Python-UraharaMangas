class Manga:
    def __init__(self, nome, volumes):
        self.nome = nome;
        self.volumes = volumes;
        self.ativo = False;

    def __str__(self):
        return f'{self.nome} | {self.volumes} | {self.ativo}';

manga_bleach = Manga("Bleach", "74");
manga_blackclover = Manga("Black Clover", "36");

mangas = [manga_bleach, manga_blackclover];

print(manga_bleach, "\n");
print(manga_blackclover, "\n");