import {
  StatisticsByTeamOrPlayer,
  StatisticsCategory,
} from '@/types/statistics'
import axios from 'axios'
import { useQuery } from 'react-query'

export default function useStatistics(statisticsCategory: StatisticsCategory) {
  return useQuery({
    queryKey: ['statistics', statisticsCategory],
    queryFn: async (): Promise<StatisticsByTeamOrPlayer[]> => {
      const { data } = await axios.get(
        `http://localhost:8000/statistics/overview?category=${statisticsCategory}`,
      )
      return data
    },
  })
}
