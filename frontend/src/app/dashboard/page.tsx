import StatisticsTable from '@/components/statistics/StatisticsTable'
import { StatisticsCategory } from '@/types/statistics'
import { Title } from '@mantine/core'

export default function DashboardPage() {
  return (
    <>
      <Title order={1} m="xl" ta="center">
        Dashboard
      </Title>
      <StatisticsTable category={StatisticsCategory.All} />
    </>
  )
}
