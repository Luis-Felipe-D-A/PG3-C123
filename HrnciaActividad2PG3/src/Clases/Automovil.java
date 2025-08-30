/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clases;

/**
 *
 * @author luisd
 */
public class Automovil extends Vehiculo {

    private String marca;
    private String modelo;
    private double precio;

    public Automovil(String FechaDEfabricacion, String VIN_chasis, String VINMotor,String marca, String modelo, double precio) {
        super(FechaDEfabricacion, VIN_chasis, VINMotor);
        this.marca = marca;
        this.modelo = modelo;
        this.precio = precio;

    }

    public void mostrarDatos(){
        System.out.println("Fecha de fabricacion: " + getFechaDEfabricacion());
        System.out.println("Numero de chasis: " + getVIN_chasis());
        System.out.println("Numero de motor: " + getVINMotor());
        System.out.println("Marca : " + getMarca());
        System.out.println("Modelo: " + getModelo());
        System.out.println("Precio: " + getPrecio());
        
    }

    /**
     * @return the marca
     */
    public String getMarca() {
        return marca;
    }

    /**
     * @param marca the marca to set
     */
    public void setMarca(String marca) {
        this.marca = marca;
    }

    /**
     * @return the modelo
     */
    public String getModelo() {
        return modelo;
    }

    /**
     * @param modelo the modelo to set
     */
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    /**
     * @return the precio
     */
    public double getPrecio() {
        return precio;
    }

    /**
     * @param precio the precio to set
     */
    public void setPrecio(double precio) {
        this.precio = precio;
    }



}
