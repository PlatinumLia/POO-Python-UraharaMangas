class Manga:
    mangas = [];

    def __init__(self, nome, volumes):
        self.nome = nome;
        self.volumes = volumes;
        self._ativo = False;
        Manga.mangas.append(self);

    def __str__(self):
        return f"{self.nome} | {self.volumes} | {self.ativo}";

    def listar_mangas():
        print("""
            ██████████████████████████████████████████████████████████████████████▀█████████████
            █▄─██─▄█▄─▄▄▀██▀▄─██─█─██▀▄─██▄─▄▄▀██▀▄─████▄─▀█▀─▄██▀▄─██▄─▀█▄─▄█─▄▄▄▄██▀▄─██─▄▄▄▄█
            ██─██─███─▄─▄██─▀─██─▄─██─▀─███─▄─▄██─▀─█████─█▄█─███─▀─███─█▄▀─██─██▄─██─▀─██▄▄▄▄─█
            ▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
              """);
        print(f"{"Nome do mangá".ljust(2)} | {"Volumes".ljust(2)} | {"Ativo"}");

        for manga in Manga.mangas:
            print(f"{manga.nome.ljust(13)} | {manga.volumes.ljust(7)} | {manga.ativo}");

    @property
    def ativo(self):
        return "✘ não ativo" if self._ativo else "✔ ativo";

manga_bleach = Manga("Bleach", "74");
manga_blackclover = Manga("Black Clover", "36");

mangas = [manga_bleach, manga_blackclover];

Manga.listar_mangas();