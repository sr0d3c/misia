/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package isia.serviciosweb;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import isia.servicios.ServiciosISIA;

/**
 *
 * @author sicuma
 * Para evitar problemas en Tomcat, esto debe desplegarse con la política:
 * 
grant codeBase "jar:file:${catalina.base}/webapps/ISIA_Web_Services/-" {
        permission java.security.AllPermission;
};
 * en el fichero catalina.policy.
 * Además, el Tomcat debe arrancarse desde un entorno en el que reconozca que hay 
 * una interfaz gráfica. Por ejemplo, desde el propio NetBeans.
 */
@WebService(serviceName = "ServiciosWebISIA")
public class ServiciosWebISIA {

    /**
     * This is a sample web service operation
     */
    @WebMethod(operationName = "hello")
    public String hello(@WebParam(name = "name") String txt) {
        return "Hello " + txt + " !";
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "getLetraDNI")
    public char getLetraDNI(@WebParam(name = "dni") int dni) {
        return ServiciosISIA.letraDNI(dni);
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "nubeEtiquetas")
    public byte[] nubeEtiquetas(@WebParam(name = "URL") String URL) {
        return ServiciosISIA.nubeEtiquetas(URL);
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "ayuda")
    public byte[] ayuda(@WebParam(name = "x") String x) {
        return new byte[100];
    }
}
