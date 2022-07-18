import java.io.BufferedReader
import java.io.File
import java.io.FileReader
import java.io.IOException
import java.nio.file.Files
import java.nio.file.Paths


const val directory: String = "C:/Users/sergi/Desktop/misia/social_computing/genomas/genomas"
const val text: String = "wax synthase"

fun buscar(dir: String, txt: String){
    Files.walk(Paths.get(dir)).use{

        paths -> paths.filter{Files.isRegularFile(it)}.forEach {
        var d: String = it.toString()
        var show: Boolean = false
        var lines = mutableListOf<String>()
        var result: Boolean = false
        var file = File(d)
        try{
            BufferedReader(FileReader(file)).use{ br ->
                var line:String?
                while (br.readLine().also { line = it } != null){
                    result = line!!.contains(txt)
                    if(result){
                        lines.add(line.toString()!!)
                        show = true
                    }
                }
                br.close()
                if(show){
                    println(d)
                    for(l in lines) println(l)
                }
            }
        } catch(e: IOException){
            e.printStackTrace()
        }
        }
    }
}


fun main() {

    buscar(directory, text)
}