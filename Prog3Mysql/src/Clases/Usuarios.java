/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clases;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
/**
 *
 * @author inarvaez
 */
public class Usuarios {
    
    private final Conector con;
    
    public Usuarios(){
        con = new Conector();
    }
    
    public void insertarUsuarios(String nombre, String apellido, String email, String telefono, String nickname, String clave){
    
    String sql = "INSERT INTO usuarios(nombre, apellido, email, telefono,nickname,clave) VALUES (?,?,?,?,?,?)";
    
    try(PreparedStatement ps = con.prepararStatement(sql)){
        ps.setString(1, nombre);
        ps.setString(2, apellido);
        ps.setString(3, email);
        ps.setString(4, telefono);
        ps.setString(5, nickname);
        ps.setString(6, clave);
        ps.execute();
        
        System.out.println("Usuario registrado correctamente");
    }catch(SQLException e){
        System.out.println("Error insertando usuario " +e.getMessage());
    }finally{
        con.desconectar();
    }
    
    }
    
}