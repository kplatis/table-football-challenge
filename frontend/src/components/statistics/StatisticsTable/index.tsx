'use client'

import useStatistics from '@/hooks/useStatistics'
import { StatisticsCategory } from '@/types/statistics'
import { Center, Loader, Table } from '@mantine/core'

type Props = {
  category: StatisticsCategory
}

export default function StatisticsTable({ category }: Props) {
  const { isLoading, data } = useStatistics(category)
  if (isLoading) {
    return (
      <Center>
        <Loader color="blue" data-testid="loader" />
      </Center>
    )
  }
  if (data) {
    const rows = data.map((statistics) => (
      <Table.Tr key={statistics.name}>
        <Table.Td>{statistics.name}</Table.Td>
        <Table.Td>{statistics.wins}</Table.Td>
        <Table.Td>{statistics.losses}</Table.Td>
        <Table.Td>{statistics.win_ratio}</Table.Td>
        <Table.Td>{statistics.goals_for}</Table.Td>
        <Table.Td>{statistics.goals_against}</Table.Td>
        <Table.Td>{statistics.goals_difference}</Table.Td>
      </Table.Tr>
    ))

    return (
      <Table mt="lg" data-test-id="statistics-table">
        <Table.Thead>
          <Table.Tr>
            <Table.Th>Name</Table.Th>
            <Table.Th>Wins</Table.Th>
            <Table.Th>Losses</Table.Th>
            <Table.Th>Win Ratio</Table.Th>
            <Table.Th>Goals For</Table.Th>
            <Table.Th>Goals Against</Table.Th>
            <Table.Th>Goals Difference</Table.Th>
          </Table.Tr>
        </Table.Thead>
        <Table.Tbody>{rows}</Table.Tbody>
      </Table>
    )
  }
  return <></>
}
