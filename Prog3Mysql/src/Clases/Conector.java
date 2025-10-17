/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

package Clases;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Conector {
    
    // Ajusta los valores según tu configuración
    private static final String URL = "jdbc:mysql://localhost:3307/pg3mysql";
    private static final String USER = "root";
    private static final String PASSWORD = "";
    
    private Connection conexion;

    // Conectar a la BD
    public Connection conectar() {
        try {
            if (conexion == null || conexion.isClosed()) {
                conexion = DriverManager.getConnection(URL, USER, PASSWORD);
                System.out.println("✅ Conexión exitosa");
            }
        } catch (SQLException e) {
            System.out.println("❌ Error de conexión: " + e.getMessage());
        }
        return conexion;
    }

    // Preparar una sentencia SQL
    public PreparedStatement prepararStatement(String sql) throws SQLException {
        Connection conn = conectar();
        if (conn == null) {
            throw new SQLException("No se pudo establecer la conexión a la BD");
        }
        return conn.prepareStatement(sql);
    }

    // Ejecutar consulta (SELECT)
    public ResultSet ejecutarConsulta(PreparedStatement ps) throws SQLException {
        return ps.executeQuery();
    }

    // Ejecutar actualización (INSERT, UPDATE, DELETE)
    public int ejecutarUpdate(PreparedStatement ps) throws SQLException {
        return ps.executeUpdate();
    }

    // Cerrar conexión
    public void desconectar() {
        try {
            if (conexion != null && !conexion.isClosed()) {
                conexion.close();
                System.out.println("🔒 Conexión cerrada");
            }
        } catch (SQLException e) {
            System.out.println("⚠️ Error al desconectarse: " + e.getMessage());
        }
    }
}
