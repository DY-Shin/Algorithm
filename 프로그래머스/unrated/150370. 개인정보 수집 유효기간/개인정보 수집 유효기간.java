import java.util.*;

class Date {
    int year;
    int month;
    int day;
    
    Date(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }
}

class Term {
    String p;
    int month;
    
    Term(String p, int month) {
        this.p = p;
        this.month = month;
    }
}

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new ArrayList<>();
        Date todayDate = stringToDate(today);
        List<Term> termList = new ArrayList<>();
        for (int i = 0; i < terms.length; i++) {
            StringTokenizer st = new StringTokenizer(terms[i]);
            String p = st.nextToken();
            int month = Integer.parseInt(st.nextToken());
            termList.add(new Term(p, month));
        }
        for (int i = 0; i < privacies.length; i++) {
            String[] now = privacies[i].split(" ");
            String nowDate = now[0];
            String pv = now[1];
            int pvMonth = 0;
            for (int j = 0; j < termList.size(); j++) {
                if (termList.get(j).p.equals(pv)) {
                    pvMonth = termList.get(j).month;
                }
            }
            Date expire = stringToDate(nowDate);
            if (expire.month + pvMonth > 12) {
                int plusYear = (expire.month + pvMonth) / 12;
                expire.year += plusYear;
                expire.month += pvMonth - 12 * plusYear;
                if (expire.month == 0) {
                    expire.year--;
                    expire.month = 12;
                }
            } else {
                expire.month += pvMonth;
            }
            if (todayDate.year > expire.year) {
                answer.add(i + 1);
            } else if (todayDate.year == expire.year){
                if (todayDate.month > expire.month) {
                    answer.add(i + 1);
                } else if (todayDate.month == expire.month) {
                    if (todayDate.day >= expire.day) {
                    answer.add(i + 1);
                    }
                }
            }
        }
        int[] result = answer.stream().mapToInt(i -> i).toArray();
        return result;
    }
    
    public Date stringToDate(String date) {
        int[] tmpDate = Arrays.stream(date.split("\\."))
            .mapToInt(Integer::parseInt)
            .toArray();
        Date todayDate = new Date(tmpDate[0], tmpDate[1], tmpDate[2]);
        return todayDate;
    }
    
}