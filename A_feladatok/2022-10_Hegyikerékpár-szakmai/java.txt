class Versenytav {
    private String rajtSzam;

    public String getTav() {
        switch (rajtSzam.charAt(0)) {
            case 'M':
                return "Mini";
            case 'R':
                return "Rövid";
            case 'K':
                return "Közép";
            case 'H':
                return "Hosszú";
            case 'E':
                return "Pedelec";
            default:
                return "Hibás rajtszám";
        }
    }

    public Versenytav(String rajtszam) {
        rajtSzam = rajtszam;
    }
}