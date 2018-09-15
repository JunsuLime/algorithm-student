import java.util.*;

class Stage implements Comparable<Stage> {

    private int id;
    private int reached;
    private double failure = 0;

    public Stage(int id) {
        this.id = id;
    }

    public void incrementReached() {
        reached++;
    }

    public int updateFailure(int cleared) {
        if (reached != 0) {
            failure = reached / (cleared + reached);
        }
        return cleared + reached;
    }

    @Override
    public int compareTo(Stage s) {
        if (failure == s.failure) {
            return id > s.id ? 1 : -1;
        }

        return failure < s.failure ? 1 : -1;
    }
}

class Solution {
    
    public int[] solution(int n, int[] raw_stages) {
        // 1) initialize all stages
        List<Stage> stages = new ArrayList();
        // input stage value 1 ~ n+1, so for 1 ~ n+1
        for (int i = 1; i <= n+1; i++) {
            stages.add(new Stage(i));
        }

        // 2) update reached num in each stages
        for (int s : raw_stages) {
            stages.get(s-1).incrementReached();
        }

        // 3) accumulate cleared and calculate failure
        int cleared = stages.get(stages.size()-1);
        stages.remove(stages.size()-1);
        for (int i = n; i >= 0; i--) {
            cleared = stages.updateFailure(cleared);   
        }

        Collections.sort(stages);
        return stages.toArray(new int[stages.size()]);
    }
}

