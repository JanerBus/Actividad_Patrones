public class Logger {
    private static Logger instancia;

    private Logger() {
        // Constructor privado para evitar instanciación directa
    }

    public static Logger obtenerInstancia() {
        if (instancia == null) {
            instancia = new Logger();
        }
        return instancia;
    }

    public void registrarInformacion(String mensaje) {
        // Lógica para registrar un mensaje de información
        System.out.println("INFO: " + mensaje);
    }

    // Métodos similares para registrar advertencias, errores, etc.
}
