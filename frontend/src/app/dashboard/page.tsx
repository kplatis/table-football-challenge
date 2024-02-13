import StatisticsDashboard from '@/components/statistics/StatisticsDashboard'
import { Title } from '@mantine/core'

export default function DashboardPage() {
  return (
    <>
      <Title order={1} m="xl" ta="center">
        Dashboard
      </Title>

      <StatisticsDashboard />
    </>
  )
}
