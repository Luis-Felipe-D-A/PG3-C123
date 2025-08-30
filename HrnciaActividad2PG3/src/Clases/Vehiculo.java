/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clases;

/**
 *
 * @author luisd
 */
public class Vehiculo {

    private String FechaDEfabricacion;
    private String VIN_chasis;
    private String VINMotor;

    public Vehiculo(String FechaDEfabricacion, String VIN_chasis, String VINMotor) {
        this.FechaDEfabricacion = FechaDEfabricacion;
        this.VIN_chasis = VIN_chasis;
        this.VINMotor = VINMotor;

      
    }

    /**
     * @return the FechaDEfabricacion
     */
    public String getFechaDEfabricacion() {
        return FechaDEfabricacion;
    }

    /**
     * @param FechaDEfabricacion the FechaDEfabricacion to set
     */
    public void setFechaDEfabricacion(String FechaDEfabricacion) {
        this.FechaDEfabricacion = FechaDEfabricacion;
    }

    /**
     * @return the VIN_chasis
     */
    public String getVIN_chasis() {
        return VIN_chasis;
    }

    /**
     * @param VIN_chasis the VIN_chasis to set
     */
    public void setVIN_chasis(String VIN_chasis) {
        this.VIN_chasis = VIN_chasis;
    }

    /**
     * @return the VINMotor
     */
    public String getVINMotor() {
        return VINMotor;
    }

    /**
     * @param VINMotor the VINMotor to set
     */
    public void setVINMotor(String VINMotor) {
        this.VINMotor = VINMotor;
    }
}
