package org.koreait.trend.entities;

import lombok.Data;

import java.util.Map;

@Data
public class CollectedTrend {
    private String image;
    private Map<String, Integer> keywords;
}
