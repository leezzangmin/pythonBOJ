import java.io.*;
import java.math.*;
import java.nio.charset.StandardCharsets;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;
import java.net.*;

class Result {

    /*

국가 이름과 전화번호가 주어지면 https://jsonmock.hackerrank.com/api/countries?name=country에서 API를 쿼리하여 국가의 호출 코드를 가져옵니다.

전화번호 앞에 호출 코드를 추가하고 문자열을 반환합니다.

 데이터 배열이 비어 있으면 문자열 -1을 반환합니다. 호출 코드가 여러 개인 경우 가장 높은 색인에 있는 코드를 사용하십시오. 숫자 형식은 다음과 같아야 합니다.

     * Complete the 'getPhoneNumbers' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. STRING country
     *  2. STRING phoneNumber
     * API URL: https://jsonmock.hackerrank.com/api/countries?name=<country>
     */

    public static String parseJsonToCallingCodesString(String jsonString) {
        String jsonString2 = "{\"page\":1,\"per_page\":10,\"total\":1,\"total_pages\":1,"
            + "\"data\":[{\"name\":\"Afghanistan\",\"nativeName\":\"افغانستان\",\"topLevelDomain\":[\".af\"]"
            + ",\"alpha2Code\":\"AF\",\"numericCode\":\"004\",\"alpha3Code\":\"AFG\",\"currencies\":[\"AFN\"]"
            + ",\"callingCodes\":[\"93\"],\"capital\":\"Kabul\",\"altSpellings\":[\"AF\",\"Afġānistān\"],\"relevance\":\"0\""
            + ",\"region\":\"Asia\",\"subregion\":\"Southern Asia\",\"language\":[\"Pashto\",\"Dari\"],\"languages\":[\"ps\",\"uz\",\"tk\"]"
            + ",\"translations\":{\"de\":\"Afghanistan\",\"es\":\"Afganistán\",\"fr\":\"Afghanistan\",\"it\":\"Afghanistan\",\"ja\":\"アフガニスタン\""
            + ",\"nl\":\"Afghanistan\",\"hr\":\"Afganistan\"},\"population\":26023100,\"latlng\":[33,65],\"demonym\":\"Afghan\",\"borders\":[\"IRN\",\"PAK\",\"TKM\""
            + ",\"UZB\",\"TJK\",\"CHN\"],\"area\":652230,\"gini\":27.8,\"timezones\":[\"UTC+04:30\"]}]})";


        for (int i=1; i < jsonString.length()-16; i++) {

            if (jsonString.substring(i, i+16).startsWith("callingCodes\":[")) {
                jsonString = jsonString.substring(i + 16);
                break;
            }
        }
        System.out.println("jsonString = " + jsonString);
        if (jsonString.startsWith("{\"page\":")) {
            return "-1";
        }

        int i=0;
        while (jsonString.charAt(i) != ']') {
            i+=1;
        }
        String a =jsonString.substring(0,i);
        String[] numberStrings = a.split(",");
        String numberString = numberStrings[numberStrings.length-1].replace("\"","");


        return "+" + numberString;
    }

    public static String getPhoneNumbers(String country, String phoneNumber) {
        String encodedCountry = URLEncoder.encode(new String(country.getBytes(StandardCharsets.UTF_8)));
        HttpURLConnection conn = getHttpURLConnection(encodedCountry);
        String jsonString = generateJsonString(conn);
        String callingCode = parseJsonToCallingCodesString(jsonString);
        if (callingCode.equals("-1")) {
            return "-1";
        }
        return callingCode + " " + phoneNumber;

    }

    private static String generateJsonString(HttpURLConnection conn) {
        StringBuffer sb = new StringBuffer();
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
            while(br.ready()) {
                sb.append(br.readLine());
            }
        } catch(Exception e) {
            e.printStackTrace();
        }
        return sb.toString();
    }

    private static HttpURLConnection getHttpURLConnection(String country) {
        HttpURLConnection conn = null;
        try {
            URL url = new URL("https://jsonmock.hackerrank.com/api/countries?name=" + country);
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-type", "application/json");
            conn.setDoOutput(true);
        } catch (Exception e) {}

        return conn;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {

        String result = Result.getPhoneNumbers("Puerto Rico", "656445445");
        System.out.println("result = " + result);
//        String sdf = Result.parseJsonToCallingCodesString("sdf");
//        System.out.println("sdf = " + sdf);

    }
}
