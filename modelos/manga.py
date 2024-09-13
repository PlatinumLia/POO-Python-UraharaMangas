class Manga:
    mangas = [];

    def __init__(self, nome, volumes):
        self.nome = nome;
        self.volumes = volumes;
        self.ativo = False;
        Manga.mangas.append(self);

    def __str__(self):
        return f'{self.nome} | {self.volumes} | {self.ativo}';

    def listar_mangas():
        for manga in Manga.mangas:
            print(f'{manga.nome} | {manga.volumes}');

manga_bleach = Manga("Bleach", "74");
manga_blackclover = Manga("Black Clover", "36");

mangas = [manga_bleach, manga_blackclover];

Manga.listar_mangas();